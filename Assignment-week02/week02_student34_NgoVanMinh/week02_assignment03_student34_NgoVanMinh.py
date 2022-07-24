def foo(name:str, idsd:int, week:str, idhw: int):
    return f"{week}_assignment0{idhw}_student{idsd}_{name}.py"

if __name__ == '__main__':
    print(foo('NgoVanMinh',34,'week_01',3))
    #week_01_assignment03_student34_NgoVanMinh.py