###### convert to snake case and kebab case
cam_cased='ThisIsCamelCased'
upper_case='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def convert_case(cam,to):
    case=[]
    case.append(cam[0].lower())
    for i in cam[1:]:
        if i in upper_case:
            if to=='snakecase':
                case.append('_')
            else:
                case.append('-')
            case.append(i.lower())
            
        else:
            case.append(i)
    if to=='snakecase':      
        print('snake_case : ',''.join(case))
    else:
        print('kebab_case : ',''.join(case))

    
print('Input camcased : ',cam_cased)
convert_case(cam_cased,'snakecase')
convert_case(cam_cased,'kebabcase')