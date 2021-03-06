#######################################################
# 
# ArgToMenuVerifier.py
# Python implementation of the Class ArgToMenuVerifier
# Generated by Enterprise Architect
# Created on:      14-Aug-2019 10:12:03 AM
# Original author: talve
# 
#######################################################


class ArgToMenuVerifier:
    """this class is responsible for verify that user input is legit by matching it
    with the menu segment.
    """
    @classmethod
    def verify(cls, menu_segment, **kwargs):
        """the method verifies that the user input is legit by matching it with the menu
        segment by calling MenuSegment.is_supported(...).
        """
        return menu_segment.is_supported(**kwargs)
