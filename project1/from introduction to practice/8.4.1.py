#-*-coding:utf-8-*-
# unprinted_designs = ['iphone case','robot pendant','dodecahedron']
# completed_models = []
# while unprinted_designs:
#     current_models = unprinted_designs.pop()
#     print("Printing models: " + current_models)
#     completed_models.append(current_models)
#
# print("The following models have been printed: ")
# for completed_model in completed_models:
#     print(completed_model)


# 编写两个执行更具体工作的函数,以上代码的优化
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)
def show_completed_models(completed_models):
    print("The following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models =[]

# 调用函数
print_models(unprinted_designs[:],completed_models)
print(unprinted_designs)
show_completed_models(completed_models)