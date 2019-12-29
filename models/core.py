# #!/usr/bin/python
# # -*- coding: utf-8 -*-
# from sqlalchemy.ext.declarative import declarative_base
#
#
# class Base:
#     """
#     This class is used to wrap framework base class into our data layer
#     """
#     __model_integrator__ = declarative_base()
#
#     @classmethod
#     def change_integrator(cls, integrator: object):
#         """
#         This class is used to change the default integrator object in order to use other framework
#         """
#         cls.__model_integrator__ = integrator
#         return cls.__model_integrator__
