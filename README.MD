Query Optimization Checker - Colab Tool

**STEP 1: Download File**
**STEP 2: Update config.py with your CLIENT ID / CLIENT SECRET for Goolge Could (*Ensure Search Console API is activated)**
**STEP 3: Upload files to Google Drive**
**STEP 4: Tool should be ready to use! - Update the "Input Variables" in the colab file with your desired Search Console property.**

############################################
############################################
############################################

```bash
< PROJECT ROOT >  
   |  
   |-- api/  
   |    |-- google/                              # **API / OAuth Flow** - Google Cloud OAuth Package   
   |    |       |-- __init__.py                  # **API / OAuth Flow** - OAuth Flow Definition 
   |    |-- google_search_console/               # **API / OAuth Flow** - GSC API Package   
   |    |       |-- __init__.py                  # **API / OAuth Flow** - Initializes `google_search_console` Package  
   |    |       |-- errors.py                    # **API / OAuth Flow** - Error Handles for GSC API  
   |    |       |-- gsc.py                       # **API / OAuth Flow** - GSC API Data Aggregation
   |    |-- __init__.py                          # **API / OAuth Flow**  - Defines `api` Package  
   |    |-- config.py                            # **API / OAuth Flow** - Defines Data Request Criteria  
   |-- semrush_data_generator.py                 # **CORE SCRIPT** - Core Script  
```