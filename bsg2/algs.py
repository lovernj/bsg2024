from bsg2 import bsg
def target_two_select(select_1: bsg.select, 
                      select_2: bsg.select,
                      holds: list[tuple[int,bsg.text,int,str]],
                      maximize:bsg.text,
                      tqdm_stats):    
    """Given two bsg.select objects, maximize the value of a bsg.text
       while constrained within holds.
       Holds is a list of tuples such that x[0] <= bsg.text <= x[1].
       x[2] in holds describes if the hold `asc`ends or `desc`ends as we
       increase select_1 and select_2. It's only used for optimization: If any hold
       is above/below the lower/upper boundary, it's pointless to continue running 
       the inner loop. """
    tmp = []
    for s1_opt in select_1.options:
        select_1.value = s1_opt
        for s2_opt in select_2.options:
            select_2.value = s2_opt
            if all(x[0]<=x[1].value<=x[2] for x in holds):
                tmp.append((s1_opt,s2_opt,[x[1].value for x in holds],maximize.value))
            if any(x[0]>x[1].value if x[3]=='desc' else x[2]<x[1].value for x in holds):
                break

    tmp = min(tmp,key=lambda x:x[3])
    select_1.value = tmp[0]
    select_2.value = tmp[1]
    print(tqdm_stats[0],tmp)


def optimize_production(env:bsg.environment,region:str, models:str, rr:tuple[float,float], sq:tuple[float,float]):
    """Optimize production for one region in two steps:\n
    1. Set the reject rate to within the bounds from `rr`, minimizing cost per pair
    2. Set the S/Q rating to within the bounds from `sq`, minimizing cost per pair"""
    print("Running optimizer for",region)
    #Set the assumptions
    env.bsg.brandprod[region].models.value = models
 
    # Manage reject rate
    target_two_select(env.bsg.comptrain[region].incentive,
                    env.bsg.brandprod[region].tqm,
                    [(rr[0],env.bsg.brandprod[region].rej_rate,rr[1],'desc')],
                    env.bsg.brandprod[region].cost_pp,
                    f"optimize_production_{region}_1")
    # then set superior material/features 
    target_two_select(env.bsg.brandprod[region].supmat,
                    env.bsg.brandprod[region].features,
                    [(sq[0],env.bsg.brandprod[region].SQ,sq[1],'asc')],
                    env.bsg.brandprod[region].cost_pp,
                    f"optimize_production_{region}_2")
    print(region, "finished")
    
def optimize_PL(env:bsg.environment,region:str, sq:float):
    """Optimize private label production for one region in one step."""
    sq[0] = max(env.bsg.privlabel.glob_min.value,sq[0]) #Force SQ to be at least global minimum
    target_two_select(env.bsg.privlabel[region].supmat,
                      env.bsg.privlabel[region].features,
                      [(sq[0],env.bsg.privlabel[region].SQ,sq[1],'asc')],
                      env.bsg.privlabel[region].cost_pp)
    
def optimize_shipping(env:bsg.environment,reg_prio):
    """Calculate optimum shipping values. Sometimes if there's significant differences
    between source regions, shipping will need to be recalculated multiple times."""
    ordered_regions = ['NA','EA','AP','LA']
    dw = env.bsg.distrware
    tot_sup = {x: dw[x].pair_avail.value for x in ordered_regions}
    real_supply = sum(tot_sup.values())
    # print(f"{real_supply}k shoes are avaiable for sale.")

    tot_req = {x: dw[x].demand.value + dw[x].req_inv.value - dw[x].beg_inv.value for x in ordered_regions}
    real_demand = sum(tot_req.values())
    # print(f"{real_demand}k shoes are needed.\n")

    spare_supply = real_supply-real_demand
    # print(f"{spare_supply}k shoes are available as spare supply which can be "
    #     f"divided evenly into {spare_supply//4}k shoes per region with "
    #     f"{spare_supply%4}k leftover to allocate.\n")

    ss_per_reg = spare_supply // 4

    for key,value in tot_req.items(): tot_req[key] += ss_per_reg
    # print(f"In total, the following needs to be sent to each region:")
    # print(*(f'{k}: {v:>6}\t' for k,v in tot_req.items()))

    shipping_dict = {x: {y: 0 for y in ordered_regions} for x in ordered_regions}

    for region in ordered_regions:
        if tot_sup[region]>0 and tot_req[region]>0:
            shipping_dict[region][region] = min(tot_sup[region],tot_req[region])
            tot_sup[region] -= shipping_dict[region][region]
            tot_req[region] -= shipping_dict[region][region]
    #print('The following shipments were done within-region:')
    #print(*(f'{k}: {shipping_dict[k][k]:>6}\t' for k in ordered_regions))

    #print('We now proceed by shipping from specific regions to specific regions')
    for fregion in reg_prio[:-1]:
        for tregion in reg_prio[:0:-1]:
            if tot_sup[fregion] == 0 or tot_req[tregion] == 0:
                continue
            shipment = min(tot_sup[fregion],tot_req[tregion])
            # print(f"{fregion} has {tot_sup[fregion]}k shoes available. Shipping {shipment} to {tregion}")
            tot_sup[fregion] -= shipment
            tot_req[tregion] -= shipment
            shipping_dict[fregion][tregion] = shipment
    #print('The final dict looks like this:')
    #print('     |',*(f'{x:^6}|' for x in ordered_regions))
    #for region in ordered_regions:
    #    print(f'{region:>5}|',*(f'{shipping_dict[x][region]:>6}|' for x in ordered_regions))

    for fregion in ordered_regions:
        for tregion in ordered_regions:
            dw[fregion]['to_'+tregion].value = shipping_dict[fregion][tregion]
    dw.NA.to_NA.elem.click() # for whatever reason, this has to happen to apply the last value.    