from typing import Callable
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

class atdict(dict):
    __getattr__= dict.__getitem__
    __setattr__= dict.__setitem__
    __delattr__= dict.__delitem__

class environment:
    """Encapsulates the state of a BSG window, including the driver and all the elements."""
    def __init__(self,driver:webdriver.Firefox):
        self.driver = driver        
        
        
        self.touched_elems = dict()
        """Keeps track of elements of the BSG that have been touched. Allows for BSG
        changes to replay between environments"""
        
        self.bsg = atdict()
        """Holds all the "actual elements" of the BSG."""
        
        self._current_page = None
        self._page_index = 0

    @property
    def page_index(self)->int:
        """State counter to determine if an element is out-of-date"""
        return self._page_index

    @property
    def page(self)->str:
        """What page is the BSG on?"""
        return self._current_page
    
    # List of pages
    # 'Compensation & Training':    endpoint("comp-training")
    # 'Branded Production':         endpoint("branded-production")
    # 'Production Facilities':      endpoint("production-equipment")
    # 'Distribution & Warehouse':   endpoint("dist-ops")
    # 'Internet Marketing':         endpoint("internet-marketing")
    # 'Wholesale Marketing':        endpoint("wholesale-marketing")
    # 'Private-Label Operations':   endpoint("private-label")
    # 'Celebrity Endorsements':     endpoint("celebrities")
    # 'Corporate Citizenship':      endpoint("csrc")
    # 'Finance & Cash Flow':        endpoint("finance")
    @page.setter
    def page(self,new_page:str):
        if self._current_page != new_page:
            self.driver.find_element(By.XPATH,f'//a[@href="/users/program/v3/decisions/{new_page}"]').click()
            self._current_page = new_page
            self._page_index += 1

    def invalidate_page(self)->None:
        """Increment the """
        self._current_page = None
        self._page_index += 1
    
    def __iadd__(self,other):
        """x += y: Add y to the touched elements of x"""
        if not issubclass(type(other),element):
            raise TypeError(f"unsupported operand type(s) for +=: {type(self)} and {type(other)}")
        self.touched_elems[(type(other),other.page,other.selector)] = other.value
        return self

    def __ilshift__(self, other):
        """x <<= y: Apply touched_elems from y to x. """
        if type(other) is not environment:
            raise TypeError(f"unsupported operand type(s) for <<: {type(self)} and {type(other)}")
        
        for selector,value in other.touched_elems.items():
            self.touched_elems[selector] = value
            selector[0](self,*selector[1:]).value = value
        return self
    
class element:
    """Base class for BSG elements. Maintains page and selector, and defines 
       the basic select operation"""
    def __init__(self,env:environment,page:str,selector:str|tuple[str,str]):
        self.page = page
        if type(selector) is str:
            self.selector = (By.XPATH,selector)
        else: 
            self.selector = selector
        self.elem = None
        self.env = env
        self.page_index = -1
        self._value = None

    def select(self)->None:
        """Set the BSG page and activate the selected element on the page.
           Call this before using self.elem"""
        if (self.env.page_index != self.page_index) or self.elem is None:
            self.env.page = self.page
            self.elem = self.env.driver.find_element(*self.selector)  
            self.page_index = self.env.page_index

    @property
    def value(self):
        """Value of HTML element this object represents"""
        self.select()
        if self._value is not None:
            return self._value
        else: raise ValueError("Element has not been initialized!")
    
    @value.setter
    def value(self,new_value):
        self.select()
        self._value = new_value
        self.env += self

class select(element):
    """A dropdown selector. Note: Do not try to set the value of disabled selectors."""
        
    def select(self)->None:
        super().select()
        self.select_elem = Select(self.elem)

    @property
    def options(self)->list[str|None]:
        """Options the selector encapsulates"""
        self.select()
        return [x.get_attribute('value') for x in self.select_elem.options]

    @property 
    def value(self)->str: return super().value
    
    @value.setter
    def value(self,value:str)->None:
        element.value.fset(self,value)
        self.select_elem.select_by_value(value)
        self.env += self

class text(element):
    """Text output. Use `format` to preformat the output (IE convert to int, or remove commas)"""
    def __init__(self,env:environment, page:str, selector:tuple[str,str], format:Callable|None = None):
        super().__init__(env,page,selector)
        self.format = format
        """Formatter that this object will apply to internal text."""

    @property
    def value(self)->str:
        self.select()
        if self.format is not None:
            return self.format(self.elem.text)
        return self.elem.text
    
class input(element):
    """Implements a value textbox."""

    @property
    def value(self)->str: return super().value
        
    @value.setter
    def value(self,value:str)->None:
        self.select()
        if self.elem.is_enabled():
            element.value.fset(self,value)
            self.elem.send_keys(Keys.BACKSPACE*15)
            self.elem.send_keys(value)