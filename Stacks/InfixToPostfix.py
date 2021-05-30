def infixToPostfix(infix_exp):
    print(infix_exp)
    postfix_exp = ""
    stack = ["("]
    print("Infix Char | ","Stack | ","POSTFIX EXPRESSION")
    for i in infix_exp:
        print(i+"\t","".join(stack)+"\t",postfix_exp)
        if i in ["/","*","%","("]:
            stack.append(i)
        elif i in ["+","-","–"]:
            if stack[-1] in ["/","*","%"]:
                postfix_exp += stack.pop()
            stack.append(i)
        elif i == ")":
            for i in reversed(stack):
                if i != "(":
                    postfix_exp += stack.pop()
                else:
                    stack.pop()
                    break 
        else:
            postfix_exp += i
    return postfix_exp



if __name__ == "__main__":
    infix_exp = input() + ")"
    postfix_exp = infixToPostfix(infix_exp.replace(" ",""))
    print("\n\n FINAL POSTFIX EXPRESSION - "+postfix_exp)