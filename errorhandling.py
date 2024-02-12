    # PYTHON ERROR HANDLING


    # COMPILE TYPE ERROR AND RUN TIME ERROR

colors = [
        "Red",
        "Green",
        "Blue",
        "white"
        ]
# print(colors[])

# try:
#     print(colors[int(input('index: '))])
# except IndexError:
#     print('Out of range. ')

# except ValueError:
#     print('Input an integer')

# except Exception as e:
#     print(f'This is the expection -{e}')

        # raise TypeError(f'This is the exception -{e}')


    # except:
    #     print('you have an error')
    # else:
    #     pass
    # finally:
    #     pass



def division():
        
    
    try:
        val1 = int(input("Enter your number: "))
        val2 = int(input("Enter your number: "))
        div = val1/val2

    except ValueError:
        print('Input an integer')
    # except Exception as e:
    #     print(e)
    except ZeroDivisionError:
        print('You have an error')

    else:
        print(div)

division()


# FILEHANDLING



