#!/usr/bin/env python

if __name__ == '__main__':

    import ballet.util.log
    import ballet.validation.main

    import ames

    ballet.util.log.enable(level='DEBUG', echo=False)
    ballet.validation.main.validate(ames)
