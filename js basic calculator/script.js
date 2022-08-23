const num1 = parseFloat(prompt("Enter first number"));
const operator = prompt("Enter operator: (+, -, /, *)");
const num2 = parseFloat(prompt("Enter second number"));

if(isNaN(num1) || isNaN(num2)){

    alert("Provide valid input for first and second number");

}else{

    let result = null;

    if(operator ==  "+"){
        result = num1 + num2;
    }else if(operator == "-"){
        result = num1 - num2;
    }else if(operator == "/"){
        result = num1 / num2;
    }else if(operator == "*"){
        result = num1 * num2;
    }else{
        alert("Invalid operator");
    }
    
    if(result != null){
        alert(`The result of ${num1} ${operator} ${num2} = ${result}`);
    }

}