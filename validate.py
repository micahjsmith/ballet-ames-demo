#!/usr/bin/env python

if __name__ == '__main__':

    from ballet.util.log import enable
    from ballet.validation.main import validate

    import ames

    enable(level='DEBUG', echo=False)
    validate(ames)
