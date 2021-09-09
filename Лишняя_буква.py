


def is_over_letter(original, modified):
    original = sorted(original)
    modified = sorted(modified)


    original += ['я'] * 1
    print (original)
    print (modified)
    
    for obj in zip(original, modified):
        if obj[0]!=obj[1]:
            return(obj[1])


if __name__  == "__main__":
     original = input()
     modified = input()
     print(is_over_letter(original, modified))
