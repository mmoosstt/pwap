import unittest
from spos.storage.db.orm import School, SchoolClass, Pupil,ValuationClass, Valuation, db, UID, ValuationGroup
from spos.server import orm as server_orm
from pony.orm import db_session, select, desc
import os
import pprint
import tempfile
from collections import OrderedDict
import json

class GlueTest(unittest.TestCase):
    from spos.glue import interface

    def setUp(self):
        db.bind(provider='sqlite', filename="test.sqlite", create_db=True)
        db.generate_mapping(create_tables=True)
        
        
    def test_school(self):
        s_school = server_orm.School()
        s_school.name = "Huber Mayer"
        s_school.id = None
        
        school = self.__class__.interface.school_new(s_school)
        school.name = "Hubert School"
        
        school = self.__class__.interface.school_edit(s_school)
        
        self.__class__.interface.school_delete(school)
        
    
    def test_get_spos(self):
        
        spos = self.__class__.interface.spos_from_storage()
        
        with open('spos.json', 'w') as f:
            f.write(spos.json())
        
        
class General(unittest.TestCase):
    
    
    def setUp(self):
        db.bind(provider='sqlite', filename="test.sqlite", create_db=True)
        db.generate_mapping(create_tables=True)
        # self.test_create()
        
    
    def tearDown(self):
        # os.remove(self.dbname)
        pass
    
    
    def test_query(self):
        with db_session:
            valuations = select((v.group.uid.uid, v.group.uid.date, v) for v in Valuation if v.pupil.uid.uid == 3)
            print(valuations.show())

    def test_load_class2(self):
        with db_session:
            school = School.select()
            school.select(sc for sc in SchoolClass if sc == school)
            
    def test_load_class(self):
        with db_session:
            
            result = []
            for school in School.select():
                dschool= OrderedDict()
                dschool['id'] = school.uid.uid
                dschool['type'] = 'school'
                dschool['name'] = school.name
                dschool['children'] = []
                
                for school_class in select(sc for sc in SchoolClass if sc.school == school):
                    dschool_class = OrderedDict()
                    dschool_class['id'] = school_class.uid.uid
                    dschool_class['type'] = 'school_class'
                    dschool_class['name'] = school_class.name
                    dschool_class['children'] = []                       

                    for pupil in select(p for p in Pupil if p.school_class == school_class):
                        dpupil = OrderedDict()
                        dpupil['id'] = pupil.uid.uid
                        dpupil['type'] = 'pupil'
                        dpupil['firstname'] = pupil.firstname
                        dpupil['surname'] = pupil.surname
                        dpupil['children'] = [] 

                        for valuation_group in select(v.group for v in Valuation if v.pupil == pupil):
                            dvaluation_group= OrderedDict()
                            dvaluation_group['id'] = valuation_group.uid.uid
                            dvaluation_group['type'] = 'valuation' 
                            dvaluation_group['date'] = str(valuation_group.uid.date) 
                            dvaluation_group['children'] = []                   
                            
                            dvaluations = {}
                            for valuation in select(v for v in Valuation if v.group == valuation_group):
                                valuation_class = ValuationClass.select(lambda vc: vc == valuation.valuation_class).first()              
                                dvaluation_group[valuation_class.grade_type] = OrderedDict()
                                dvaluation_group[valuation_class.grade_type]['grade'] = valuation_class.grade
                                dvaluation_group[valuation_class.grade_type]['grade_description'] = valuation_class.grade_description
                                  
                            dpupil['children'].append(dvaluation_group)
                          
                        dschool_class['children'].append(dpupil)  
                        
                    dschool['children'].append(dschool_class)
                
                result.append(dschool)
                  
                        
            print(json.dumps(result, indent=True))      
    
    def test_valuation_set(self):
        with db_session: 
            for x in range(10):       
                Valuation.get_valuations_of_pupil(pupil_uid)
            
        
    
    def test_create_db(self):

        with db_session:
            s = School(name="1a")
            sc = SchoolClass(name="10a", school=s)
 
            for i in range(4):
                print(i)
                p1 = Pupil(surname="roman", firstname="fuerst{}".format(i), school_class=sc)
                p2 = Pupil(surname="tobi", firstname="beutling{}".format(i), school_class=sc)
                sc.pupil.add(p1)
                sc.pupil.add(p2)           
                ValuationGroup.create_valuation_set(p1)
                ValuationGroup.create_valuation_set(p1)
                
                