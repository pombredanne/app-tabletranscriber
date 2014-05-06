# -*- coding: utf-8 -*-

class Meb_exception( Exception ):
    def __init__(self, code, msg):
        self.code = code
        self.msg = msg  
    
    def __str__(self):
        return repr(unicode(self.msg, "utf-8"))
    
    def config_msg(self, *args):
        raise NotImplemented("Should have implemented this")

class Meb_apps_exception( Meb_exception ):
    std_exception_msgs = {
           1 : "MEB-APPS-1: App with empty name",
           2 : "MEB-APPS-2: App with empty shortname",
           3 : "MEB-APPS-3: App with empty description",
           4 : "MEB-APPS-4: Error creating the application",
           5 : "MEB-APPS-5: Error you must supply values into info dict",
           6 : "MEB-APPS-6: Task must be priority between 0 and 1"
          }

    def __init__(self, exc_code, app_id, app_sh_name):
        msg = self.config_msg(exc_code, app_id, app_sh_name)
        super(Meb_apps_exception, self).__init__(exc_code, msg)
    
    def config_msg(self, exc_code, app_id, app_sh_name):
        return "%s | app_id : %d | app_short_name: %s" % (self.std_exception_msgs[exc_code], app_id, app_sh_name)
    

class Meb_ttapps_exception( Meb_apps_exception ):
    std_exception_msgs = {
           1 : "MEB-TTAPPS-1: Selection app with empty shortname",
           2 : "MEB-TTAPPS-2: Meta app with empty shortname",
           3 : "MEB-TTAPPS-3: Struct app with empty shortname",
           4 : "MEB-TTAPPS-4: Transcribe app with empty shortname",
           5 : "MEB-TTAPPS-5: Invalid selection app shortname",
           6 : "MEB-TTAPPS-6: Invalid meta app shortname",
           7 : "MEB-TTAPPS-7: Invalid struct app shortname",
           8 : "MEB-TTAPPS-8: Invalid transcribe app shortname"
          }

    def __init__(self, exc_code, app_id, app_sh_name):
        msg = super(Meb_ttapps_exception, self).config_msg(exc_code, app_id, app_sh_name)
        super(Meb_ttapps_exception, self).__init__(exc_code, app_id, app_sh_name)
        

class Meb_pb_task_exception( Meb_exception ):
    std_exception_msgs = {
           1 : "MEB-PB-TASK-1: Cannot find task",
           2 : "MEB-PB-TASK-2: Invalid shortname"
          }
       
    def __init__(self, exc_code, task_id, app_sh_name):
        msg = self.config_msg(exc_code, task_id, app_sh_name)
        super(Meb_pb_task_exception, self).__init__(exc_code, msg)
    
    def config_msg(self, exc_code, t_id, app_sh_name):
        return "%s | task_id : %d | app_short_name : %s" % (self.std_exception_msgs[exc_code], t_id, app_sh_name)   

        
class Meb_task_factory_exception( Meb_exception ):
    std_exception_msgs = {
           1 : "MEB-TASK-FACTORY-2: Task not found"
          }
       
    def __init__(self, exc_code, task_id):
        msg = self.config_msg(exc_code, task_id)
        super(Meb_task_factory_exception, self).__init__(exc_code, msg)
    
    def config_msg(self, exc_code, task_id):
        return "%s | task_id : %d" % (self.std_exception_msgs[exc_code], task_id)
    

class Archive_book_data_exception( Meb_exception ):
    std_exception_msgs = {
                          1 : "This book does not have one key"
                          }
    
    def __init__(self, exc_code, key):
        msg = self.config_msg(key)
        super(Meb_util_exception, self).__init__(exc_code, msg)
        
    def config_msg(self, exc_code, key):
        return "%s | key : %s" % (key)
    
    