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

def get_version() :
  #  codetype  b241
  submission_id = request.args[0]
  codeType = db((db.submissions.submission_id == submission_id) &  (db.submissions.context_id==db.press_settings.press_id) &  (db.press_settings.setting_name=='codeType' )).select(db.press_settings.setting_value).first()['setting_value']
  # codeValue b243
  codeValue = db((db.submissions.submission_id == submission_id) & (db.submissions.context_id==db.press_settings.press_id) & (db.press_settings.setting_name=='codeValue')).select(db.press_settings.setting_value).first()['setting_value']
  # publisher 
  publisher = db((db.submissions.submission_id == submission_id) & (db.submissions.context_id==db.press_settings.press_id) & (db.press_settings.setting_name=='publisher')).select(db.press_settings.setting_value).first()['setting_value']
  
  
  return  locals()
 
  