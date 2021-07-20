#!/usr/bin/env python
# coding: utf-8

# In[2]:


from pydantic import BaseModel

class money(BaseModel):
    jobType_CEO: int
    jobType_CFO: int
    jobType_CTO: int 
    jobType_JANITOR: int 
    jobType_JUNIOR: int
    jobType_MANAGER:int
    jobType_SENIOR:int
    jobType_VICE_PRESIDENT:int
    yearsExperience:float
    milesFromMetropolis:float
        
   

# In[ ]:





# In[ ]:





# In[ ]:




