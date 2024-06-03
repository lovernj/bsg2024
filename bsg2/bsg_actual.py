from bsg2 import bsg
from selenium.webdriver.common.by import By

def instantiate_environment(env:bsg.environment):
    """Fill the env with actual bsg elements scraped from the page."""
    env.bsg.comptrain = bsg.atdict()
    env.bsg.comptrain.NA = bsg.atdict()
    env.bsg.comptrain.NA.basewage  = bsg.select(env,'comp-training',(By.CSS_SELECTOR,'#G4-btn'))
    env.bsg.comptrain.NA.incentive = bsg.select(env,'comp-training',(By.CSS_SELECTOR,'#G5-btn'))
    env.bsg.comptrain.NA.fringe    = bsg.select(env,'comp-training',(By.CSS_SELECTOR,'#G6-btn'))
    env.bsg.comptrain.NA.bestprac  = bsg.select(env,'comp-training',(By.CSS_SELECTOR,'#G8-btn'))
    env.bsg.comptrain.NA.supstaff  = bsg.select(env,'comp-training',(By.CSS_SELECTOR,'#G10-btn'))
    env.bsg.comptrain.NA.supcomp   = bsg.select(env,'comp-training',(By.CSS_SELECTOR,'#G11-btn'))
    env.bsg.comptrain.NA.productivity = bsg.text(env,'comp-training','//glo-comp-training/div/div[4]/div/table/tbody/tr[1]/td[2]/strong',lambda x: int(x.replace(',','')))
    env.bsg.comptrain.NA.tot_cpp      = bsg.text(env,'comp-training','//glo-comp-training/div/div[5]/div/table/tbody/tr[8]/td[3]/div/span[2]/strong',lambda x: float(x))

    env.bsg.comptrain.EA = bsg.atdict()
    env.bsg.comptrain.EA.basewage  = bsg.select(env,'comp-training',(By.CSS_SELECTOR,'#G15-btn'))
    env.bsg.comptrain.EA.incentive = bsg.select(env,'comp-training',(By.CSS_SELECTOR,'#G16-btn'))
    env.bsg.comptrain.EA.fringe    = bsg.select(env,'comp-training',(By.CSS_SELECTOR,'#G17-btn'))
    env.bsg.comptrain.EA.bestprac  = bsg.select(env,'comp-training',(By.CSS_SELECTOR,'#G19-btn'))
    env.bsg.comptrain.EA.supstaff  = bsg.select(env,'comp-training',(By.CSS_SELECTOR,'#G21-btn'))
    env.bsg.comptrain.EA.supcomp   = bsg.select(env,'comp-training',(By.CSS_SELECTOR,'#G22-btn'))
    env.bsg.comptrain.EA.productivity = bsg.text(env,'comp-training','//glo-comp-training/div/div[4]/div/table/tbody/tr[1]/td[3]/strong',lambda x: int(x.replace(',','')))
    env.bsg.comptrain.EA.tot_cpp      = bsg.text(env,'comp-training','//glo-comp-training/div/div[5]/div/table/tbody/tr[8]/td[5]/div/span[2]/strong',lambda x: float(x))

    env.bsg.comptrain.AP = bsg.atdict()
    env.bsg.comptrain.AP.basewage  = bsg.select(env,'comp-training','//*[@id="G26-btn"]')
    env.bsg.comptrain.AP.incentive = bsg.select(env,'comp-training','//*[@id="G27-btn"]')
    env.bsg.comptrain.AP.fringe    = bsg.select(env,'comp-training','//*[@id="G28-btn"]')
    env.bsg.comptrain.AP.bestprac  = bsg.select(env,'comp-training','//*[@id="G30-btn"]')
    env.bsg.comptrain.AP.supstaff  = bsg.select(env,'comp-training','//*[@id="G32-btn"]')
    env.bsg.comptrain.AP.supcomp   = bsg.select(env,'comp-training','//*[@id="G33-btn"]')
    env.bsg.comptrain.AP.productivity = bsg.text(env,'comp-training','//glo-comp-training/div/div[4]/div/table/tbody/tr[1]/td[4]/strong',lambda x: int(x.replace(',','')))
    env.bsg.comptrain.AP.tot_cpp      = bsg.text(env,'comp-training','//glo-comp-training/div/div[5]/div/table/tbody/tr[8]/td[7]/div/span[2]/strong',lambda x: float(x))

    env.bsg.comptrain.LA = bsg.atdict()
    env.bsg.comptrain.LA.basewage  = bsg.select(env,'comp-training','//*[@id="G37-btn"]')
    env.bsg.comptrain.LA.incentive = bsg.select(env,'comp-training','//*[@id="G38-btn"]')
    env.bsg.comptrain.LA.fringe    = bsg.select(env,'comp-training','//*[@id="G39-btn"]')
    env.bsg.comptrain.LA.bestprac  = bsg.select(env,'comp-training','//*[@id="G41-btn"]')
    env.bsg.comptrain.LA.supstaff  = bsg.select(env,'comp-training','//*[@id="G43-btn"]')
    env.bsg.comptrain.LA.supcomp   = bsg.select(env,'comp-training','//*[@id="G44-btn"]')
    env.bsg.comptrain.LA.productivity = bsg.text(env,'comp-training','//glo-comp-training/div/div[4]/div/table/tbody/tr[1]/td[5]/strong',lambda x: int(x.replace(',','')))
    env.bsg.comptrain.LA.tot_cpp      = bsg.text(env,'comp-training','//glo-comp-training/div/div[5]/div/table/tbody/tr[8]/td[9]/div/span[2]/strong',lambda x: float(x))

    env.bsg.brandprod = bsg.atdict()

    env.bsg.brandprod.NA = bsg.atdict()
    env.bsg.brandprod.NA.supmat   = bsg.select(env,'branded-production',(By.CSS_SELECTOR,'#G55-btn'))
    env.bsg.brandprod.NA.models   = bsg.select(env,'branded-production',(By.CSS_SELECTOR,'#G56-btn'))
    env.bsg.brandprod.NA.features = bsg.select(env,'branded-production',(By.CSS_SELECTOR,'#G57-btn'))
    env.bsg.brandprod.NA.tqm      = bsg.select(env,'branded-production',(By.CSS_SELECTOR,'#G58-btn'))
    env.bsg.brandprod.NA.SQ       = bsg.text(env,'branded-production','//glo-branded-production/div/div[2]/div/table/tbody/tr[1]/td[2]/strong',lambda x:float(x[:-1]))
    env.bsg.brandprod.NA.rej_rate = bsg.text(env,'branded-production',(By.CSS_SELECTOR,'div.card:nth-child(2) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2)'),lambda x:float(x[:-1]))
    env.bsg.brandprod.NA.cost_pp  = bsg.text(env,'branded-production',(By.CSS_SELECTOR,'div.card:nth-child(8) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(3) > tr:nth-child(8) > td:nth-child(3) > div:nth-child(1) > span:nth-child(2) > strong:nth-child(1)'),lambda x: float(x))

    env.bsg.brandprod.EA = bsg.atdict()
    env.bsg.brandprod.EA.supmat   = bsg.select(env,'branded-production','//*[@id="G64-btn"]')
    env.bsg.brandprod.EA.models   = bsg.select(env,'branded-production','//*[@id="G65-btn"]')
    env.bsg.brandprod.EA.features = bsg.select(env,'branded-production','//*[@id="G66-btn"]')
    env.bsg.brandprod.EA.tqm      = bsg.select(env,'branded-production','//*[@id="G67-btn"]')
    env.bsg.brandprod.EA.SQ       = bsg.text(env,'branded-production','//glo-branded-production/div/div[2]/div/table/tbody/tr[1]/td[3]/strong',lambda x:float(x[:-1]))
    env.bsg.brandprod.EA.rej_rate = bsg.text(env,'branded-production','//glo-branded-production/div/div[2]/div/table/tbody/tr[2]/td[3]',lambda x:float(x[:-1]))
    env.bsg.brandprod.EA.cost_pp  = bsg.text(env,'branded-production','//glo-branded-production/div/div[7]/div/table/tbody/tr[8]/td[5]/div/span[2]/strong',lambda x: float(x))

    env.bsg.brandprod.AP = bsg.atdict()
    env.bsg.brandprod.AP.supmat   = bsg.select(env,'branded-production','//*[@id="G73-btn"]')
    env.bsg.brandprod.AP.models   = bsg.select(env,'branded-production','//*[@id="G74-btn"]')
    env.bsg.brandprod.AP.features = bsg.select(env,'branded-production','//*[@id="G75-btn"]')
    env.bsg.brandprod.AP.tqm      = bsg.select(env,'branded-production','//*[@id="G76-btn"]')
    env.bsg.brandprod.AP.SQ       = bsg.text(env,'branded-production','//glo-branded-production/div/div[2]/div/table/tbody/tr[1]/td[4]/strong',lambda x:float(x[:-1]))
    env.bsg.brandprod.AP.rej_rate = bsg.text(env,'branded-production','//glo-branded-production/div/div[2]/div/table/tbody/tr[2]/td[4]',lambda x:float(x[:-1]))
    env.bsg.brandprod.AP.cost_pp  = bsg.text(env,'branded-production','//glo-branded-production/div/div[7]/div/table/tbody/tr[8]/td[7]/div/span[2]/strong',lambda x: float(x))

    env.bsg.brandprod.LA = bsg.atdict()
    env.bsg.brandprod.LA.supmat   = bsg.select(env,'branded-production','//*[@id="G82-btn"]')
    env.bsg.brandprod.LA.models   = bsg.select(env,'branded-production','//*[@id="G83-btn"]')
    env.bsg.brandprod.LA.features = bsg.select(env,'branded-production','//*[@id="G84-btn"]')
    env.bsg.brandprod.LA.tqm      = bsg.select(env,'branded-production','//*[@id="G85-btn"]')
    env.bsg.brandprod.LA.SQ       = bsg.text(env,'branded-production','//glo-branded-production/div/div[2]/div/table/tbody/tr[1]/td[5]/strong',lambda x:float(x[:-1]))
    env.bsg.brandprod.LA.rej_rate = bsg.text(env,'branded-production','//glo-branded-production/div/div[2]/div/table/tbody/tr[2]/td[5]',lambda x:float(x[:-1]))
    env.bsg.brandprod.LA.cost_pp  = bsg.text(env,'branded-production','//glo-branded-production/div/div[7]/div/table/tbody/tr[8]/td[9]/div/span[2]/strong',lambda x: float(x))

    env.bsg.prodfacil = bsg.atdict()
    env.bsg.prodfacil.NA = bsg.atdict()
    env.bsg.prodfacil.EA = bsg.atdict()
    env.bsg.prodfacil.AP = bsg.atdict()
    env.bsg.prodfacil.LA = bsg.atdict()

    env.bsg.distrware = bsg.atdict()
    env.bsg.distrware.NA = bsg.atdict()
    env.bsg.distrware.NA.pair_avail = bsg.text(env,'dist-ops','//glo-dist-ops/div/div[1]/div/table/tbody/tr[1]/td[2]',lambda x: int(x.replace(',','')[:-6]))
    env.bsg.distrware.NA.to_NA      = bsg.input(env,'dist-ops','//glo-dist-ops/div/div[1]/div/table/tbody/tr[2]/td[3]/div/glo-entry-input/input')
    env.bsg.distrware.NA.to_EA      = bsg.input(env,'dist-ops','//glo-dist-ops/div/div[1]/div/table/tbody/tr[3]/td[2]/div/glo-entry-input/input')
    env.bsg.distrware.NA.to_AP      = bsg.input(env,'dist-ops','//glo-dist-ops/div/div[1]/div/table/tbody/tr[4]/td[2]/div/glo-entry-input/input')
    env.bsg.distrware.NA.to_LA      = bsg.input(env,'dist-ops','//glo-dist-ops/div/div[1]/div/table/tbody/tr[5]/td[2]/div/glo-entry-input/input')
    env.bsg.distrware.NA.beg_inv    = bsg.text(env,'dist-ops','//glo-dist-ops/div/div[3]/div/table/tbody/tr[1]/td[2]/div/span',lambda x: int(x.replace(',','')))
    env.bsg.distrware.NA.demand     = bsg.text(env,'dist-ops','//glo-dist-ops/div/div[3]/div/table/tbody/tr[7]/td[2]/div/span/strong',lambda x: int(x.replace(',','')))
    env.bsg.distrware.NA.req_inv    = bsg.text(env,'dist-ops','//glo-dist-ops/div/div[3]/div/table/tbody/tr[8]/td[2]/div/span[1]',lambda x: int(x.replace(',','')))

    env.bsg.distrware.EA = bsg.atdict()
    env.bsg.distrware.EA.pair_avail = bsg.text(env,'dist-ops','//glo-dist-ops/div/div[1]/div/table/tbody/tr[1]/td[3]',lambda x: int(x.replace(',','')[:-6]))
    env.bsg.distrware.EA.to_NA      = bsg.input(env,'dist-ops','//glo-dist-ops/div/div[1]/div/table/tbody/tr[2]/td[4]/div/glo-entry-input/input')
    env.bsg.distrware.EA.to_EA      = bsg.input(env,'dist-ops','//glo-dist-ops/div/div[1]/div/table/tbody/tr[3]/td[3]/div/glo-entry-input/input')
    env.bsg.distrware.EA.to_AP      = bsg.input(env,'dist-ops','//glo-dist-ops/div/div[1]/div/table/tbody/tr[4]/td[3]/div/glo-entry-input/input')
    env.bsg.distrware.EA.to_LA      = bsg.input(env,'dist-ops','//glo-dist-ops/div/div[1]/div/table/tbody/tr[5]/td[3]/div/glo-entry-input/input')
    env.bsg.distrware.EA.beg_inv    = bsg.text(env,'dist-ops','//glo-dist-ops/div/div[3]/div/table/tbody/tr[1]/td[5]/div/span',lambda x: int(x.replace(',','')))
    env.bsg.distrware.EA.demand     = bsg.text(env,'dist-ops','//glo-dist-ops/div/div[3]/div/table/tbody/tr[7]/td[3]/div/span/strong',lambda x: int(x.replace(',','')))
    env.bsg.distrware.EA.req_inv    = bsg.text(env,'dist-ops','//glo-dist-ops/div/div[3]/div/table/tbody/tr[8]/td[3]/div/span[1]',lambda x: int(x.replace(',','')))

    env.bsg.distrware.AP = bsg.atdict()
    env.bsg.distrware.AP.pair_avail = bsg.text(env,'dist-ops','//glo-dist-ops/div/div[1]/div/table/tbody/tr[1]/td[4]',lambda x: int(x.replace(',','')[:-6]))
    env.bsg.distrware.AP.to_NA      = bsg.input(env,'dist-ops','//glo-dist-ops/div/div[1]/div/table/tbody/tr[2]/td[5]/div/glo-entry-input/input')
    env.bsg.distrware.AP.to_EA      = bsg.input(env,'dist-ops','//glo-dist-ops/div/div[1]/div/table/tbody/tr[3]/td[4]/div/glo-entry-input/input')
    env.bsg.distrware.AP.to_AP      = bsg.input(env,'dist-ops','//glo-dist-ops/div/div[1]/div/table/tbody/tr[4]/td[4]/div/glo-entry-input/input')
    env.bsg.distrware.AP.to_LA      = bsg.input(env,'dist-ops','//glo-dist-ops/div/div[1]/div/table/tbody/tr[5]/td[4]/div/glo-entry-input/input')
    env.bsg.distrware.AP.beg_inv    = bsg.text(env,'dist-ops','//glo-dist-ops/div/div[3]/div/table/tbody/tr[1]/td[8]/div/span',lambda x: int(x.replace(',','')))
    env.bsg.distrware.AP.demand     = bsg.text(env,'dist-ops','//glo-dist-ops/div/div[3]/div/table/tbody/tr[7]/td[4]/div/span/strong',lambda x: int(x.replace(',','')))
    env.bsg.distrware.AP.req_inv    = bsg.text(env,'dist-ops','//glo-dist-ops/div/div[3]/div/table/tbody/tr[8]/td[4]/div/span[1]',lambda x: int(x.replace(',','')))

    env.bsg.distrware.LA = bsg.atdict()
    env.bsg.distrware.LA.pair_avail = bsg.text(env,'dist-ops','//glo-dist-ops/div/div[1]/div/table/tbody/tr[1]/td[5]',lambda x: int(x.replace(',','')[:-6]))
    env.bsg.distrware.LA.to_NA      = bsg.input(env,'dist-ops','//glo-dist-ops/div/div[1]/div/table/tbody/tr[2]/td[6]/div/glo-entry-input/input')
    env.bsg.distrware.LA.to_EA      = bsg.input(env,'dist-ops','//glo-dist-ops/div/div[1]/div/table/tbody/tr[3]/td[5]/div/glo-entry-input/input')
    env.bsg.distrware.LA.to_AP      = bsg.input(env,'dist-ops','//glo-dist-ops/div/div[1]/div/table/tbody/tr[4]/td[5]/div/glo-entry-input/input')
    env.bsg.distrware.LA.to_LA      = bsg.input(env,'dist-ops','//glo-dist-ops/div/div[1]/div/table/tbody/tr[5]/td[5]/div/glo-entry-input/input')
    env.bsg.distrware.LA.beg_inv    = bsg.text(env,'dist-ops','//glo-dist-ops/div/div[3]/div/table/tbody/tr[1]/td[11]/div/span',lambda x: int(x.replace(',','')))
    env.bsg.distrware.LA.demand     = bsg.text(env,'dist-ops','//glo-dist-ops/div/div[3]/div/table/tbody/tr[7]/td[5]/div/span/strong',lambda x: int(x.replace(',','')))
    env.bsg.distrware.LA.req_inv    = bsg.text(env,'dist-ops','//glo-dist-ops/div/div[3]/div/table/tbody/tr[8]/td[5]/div/span[1]',lambda x: int(x.replace(',','')))

    env.bsg.netmarket = bsg.atdict()
    env.bsg.netmarket.NA = bsg.atdict()
    env.bsg.netmarket.EA = bsg.atdict()
    env.bsg.netmarket.AP = bsg.atdict()
    env.bsg.netmarket.LA = bsg.atdict()

    env.bsg.wholemark = bsg.atdict()
    env.bsg.wholemark.NA = bsg.atdict()
    env.bsg.wholemark.EA = bsg.atdict()
    env.bsg.wholemark.AP = bsg.atdict()
    env.bsg.wholemark.LA = bsg.atdict()

    env.bsg.privlabel = bsg.atdict()
    env.bsg.privlabel.glob_min = bsg.text(env,'private-label','//glo-private-label/div/div[2]/div/table/tbody/tr/td[1]/strong/span[2]/span/strong/span[2]',lambda x:float(x[:-1]))
    env.bsg.privlabel.NA = bsg.atdict()
    env.bsg.privlabel.NA.supmat   = bsg.select(env,'private-label','//*[@id="G326-btn"]')
    env.bsg.privlabel.NA.features = bsg.select(env,'private-label','//*[@id="G327-btn"]')
    env.bsg.privlabel.NA.SQ       = bsg.text(env,'private-label','//glo-private-label/div/div[2]/div/table/tbody/tr/td[2]/span/strong',lambda x:float(x[:-1]))
    env.bsg.privlabel.NA.cost_pp  = bsg.text(env,'private-label','//glo-private-label/div/div[3]/div/table/tbody/tr[10]/td[2]/div/div[1]',lambda x: float(x[2:]))

    env.bsg.privlabel.EA = bsg.atdict()
    env.bsg.privlabel.EA.supmat   = bsg.select(env,'private-label','//*[@id="G338-btn"]')
    env.bsg.privlabel.EA.features = bsg.select(env,'private-label','//*[@id="G339-btn"]')
    env.bsg.privlabel.EA.SQ       = bsg.text(env,'private-label','//glo-private-label/div/div[2]/div/table/tbody/tr/td[3]/span/strong',lambda x:float(x[:-1]))
    env.bsg.privlabel.EA.cost_pp  = bsg.text(env,'private-label','//glo-private-label/div/div[3]/div/table/tbody/tr[10]/td[3]/div/div[1]',lambda x: float(x[2:]))

    env.bsg.privlabel.AP = bsg.atdict()
    env.bsg.privlabel.AP.supmat   = bsg.select(env,'private-label','//*[@id="G350-btn"]')
    env.bsg.privlabel.AP.features = bsg.select(env,'private-label','//*[@id="G351-btn"]')
    env.bsg.privlabel.AP.SQ       = bsg.text(env,'private-label','//glo-private-label/div/div[2]/div/table/tbody/tr/td[4]/span/strong',lambda x:float(x[:-1]))
    env.bsg.privlabel.AP.cost_pp  = bsg.text(env,'private-label','//glo-private-label/div/div[3]/div/table/tbody/tr[10]/td[4]/div/div[1]',lambda x: float(x[2:]))

    env.bsg.privlabel.LA = bsg.atdict()
    env.bsg.privlabel.LA.supmat   = bsg.select(env,'private-label','//*[@id="G362-btn"]')
    env.bsg.privlabel.LA.features = bsg.select(env,'private-label','//*[@id="G363-btn"]')
    env.bsg.privlabel.LA.SQ       = bsg.text(env,'private-label','//glo-private-label/div/div[2]/div/table/tbody/tr/td[5]/span/strong',lambda x:float(x[:-1]))
    env.bsg.privlabel.LA.cost_pp  = bsg.text(env,'private-label','//glo-private-label/div/div[3]/div/table/tbody/tr[10]/td[5]/div/div[1]',lambda x: float(x[2:]))

    env.bsg.celebrity = bsg.atdict()
    env.bsg.financial = bsg.atdict()