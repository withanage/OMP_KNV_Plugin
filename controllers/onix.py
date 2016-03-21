# The MIT License

# Copyright 16-Mar-2016, 14:30:56
#
# Author    : Dulip Withanage , University of Heidelberg
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import time
def get_version() :
  
  submission_id = request.args[0]
  publication_format_name = request.args[1]
  publication_available = ''
  publication_date = ''
  height,height_unit_code, width, width_unit_code, thickness, thickness_unit_code, weight, weight_unit_code= '', '', '', '', '', '', '', ''
    
  #  codetype  b241 
  codeType = db((db.submissions.submission_id == submission_id) &  (db.submissions.context_id==db.press_settings.press_id) &  (db.press_settings.setting_name=='codeType' )).select(db.press_settings.setting_value).first()
  if codeType is not None:
    codeType = codeType['setting_value']
  else:
    codeType = ' '
    
    
  
  # codeValue b243
  codeValue = db((db.submissions.submission_id == submission_id) & (db.submissions.context_id==db.press_settings.press_id) & (db.press_settings.setting_name=='codeValue')).select(db.press_settings.setting_value).first()
  if codeValue is not None:
    codeValue = codeValue['setting_value']
  else:
    codeValue = ''
  
  # publisher 
  publisher = db((db.submissions.submission_id == submission_id) & (db.submissions.context_id==db.press_settings.press_id) & (db.press_settings.setting_name=='publisher')).select(db.press_settings.setting_value).first()
  if publisher is not None:
    publisher = publisher['setting_value']
  else:
    publisher = ''
  
  # country_manufacture_code b083
  country_manufacture_code = db((db.publication_formats.submission_id == submission_id) & (db.publication_formats.publication_format_id == db.publication_format_settings.publication_format_id) & (db.publication_format_settings.setting_value == publication_format_name)).select(db.publication_formats.country_manufacture_code).first()
  
  if country_manufacture_code is not None:
    country_manufacture_code = country_manufacture_code['country_manufacture_code']
  else:
    country_manufacture_code = ''
    
  # publication_available b394
  publication_results = db((db.publication_formats.submission_id == submission_id)  & (db.publication_formats.publication_format_id == db.publication_format_settings.publication_format_id) & (db.publication_format_settings.setting_value == publication_format_name) & (db.publication_formats.publication_format_id == db.publication_dates.publication_format_id)).select(db.publication_formats.is_available, db.publication_dates.date).first()
  if publication_results is not None:
     if publication_results.publication_formats is not None:
       publication_available = publication_results.publication_formats['is_available']
       if publication_available == 1:
          publication_date =  publication_results.publication_dates.date
          if publication_results.publication_dates.date  > time.strftime("%Y%m%d") :
            publication_available = '02'
          else:
            publication_available = '04'
       else:
           publication_available = ''  
     else: 
       publication_available = ''
  else:
    publication_available = ''
    
  physical_info = db((db.publication_formats.submission_id == submission_id) & (db.publication_format_settings.setting_value == publication_format_name)   & (db.publication_formats.publication_format_id == db.publication_format_settings.publication_format_id)).select(db.publication_formats.height, db.publication_formats.height_unit_code, db.publication_formats.width, db.publication_formats.width_unit_code, db.publication_formats.thickness,db.publication_formats.thickness_unit_code, db.publication_formats.weight, db.publication_formats.weight_unit_code).first()
  if physical_info is not None:
     height = physical_info['height']
     height_unit_code = physical_info['height_unit_code']
     width = physical_info['width']
     width_unit_code = physical_info['width_unit_code']
     thickness = physical_info['thickness']
     thickness_unit_code = physical_info['thickness_unit_code']
     weight = physical_info['weight']
     weight_unit_code = physical_info['weight_unit_code']
  

  return  locals()
 
  