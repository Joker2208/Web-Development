
////////////Ques 1///////////////////

// console.log("This is external JS file")

////////////////Ques 2//////////////

// alert("Hello JS")
// console.log("Hello JS")
//document.write("Hello JS")

//////////////Ques 3/////////////////

// let myVar = 1;
// let myvar = 2;
// console.log(`${myVar} and ${myvar} printed as seperate values`)

/////////////////Ques 4////////////////////////////

// const name = {    //Used an object to create person information to reduce usage of extra variables.
//     firstName : "Dipesh",
//     lastName : "Tambakhe",
//     age : 29
// };
// let fname = "Full Name: " + name.firstName + " " + name.lastName + "," + " Age:"+ name.age;
// console.log(fname)
/* What this does is makes your code more shorter and easier to understand for other developer as more than 1 developer is wokring on it */


///////////////////Ques 5//////////////////////////////

// var price = 500;
// let qty = 3;
// const tax = 0.18;
// let subtotal = price * qty
// let finalTax = subtotal * tax
// let total = subtotal + finalTax
// console.log(total)


///////////////////////////////Ques 6///////////////////// //

// Try const x = 5; x = 10; inside try/catch and print the error message. Then create const arr = [1,2], push 3 and print the array. ☐ Expected: "Assignment to constant variable." and [1,2,3]

// const x = 5;
// try{
//  x= 10;
// }
// catch(err){
//     console.log(err.message)
// }


// const arr = [1,2];
// arr.push(3);
// console.log(arr)

////////////////////////////Ques 7/////////////////////

// Create one variable for each type (string, number, boolean, undefined, null, bigint, symbol, object, array, function). Print name, value and typeof using console.table. ☐

// let str = "Dipesh";
// let num = 22;
// let bool = true;
// let x;
// let y = null;
// let big =12345n;
// let sym = Symbol();
// let obj = {firstName : "Dipesh", lastName : "Tambakhe"};
// const arr = [1,2,3];

// function hello() {
//     return "Hello JS"
// }

// console.table([
//     {name : "string" , value : str , type : typeof str },
//     {name : "num" , value : num , type : typeof num },
//     {name : "boolean" , value : bool , type : typeof bool },
//     {name : "x" , value : x , type : typeof x },
//     {name : "y" , value : y , type : typeof y },
//     {name : "big" , value : big , type : typeof big },
//     {name : "symbol" , value : sym , type : typeof sym },
//     {name : "object" , value : obj , type : typeof obj },
//     {name : "array" , value : arr , type : typeof arr },
//     {name : "function" , value : hello() , type : typeof hello }

// ])

//////////////////////////////Ques 8/////////////////

// Swap the values of two variables a = 10, b = 20 using a temporary variable. Print before and after. ☐

// let a = 10, b = 20, temp;
// temp = a;
// a = b;
// b = temp;
// console.log(a,b);

/////////////////////////Ques 9/////////////////////////

// With a = 17, b = 5 print + - * / % **. Also show the difference between x++ and ++x using let x = 5. ☐

// let a = 17;
// let b = 5;
// console.log(`Add: ${a+b}, Sub: ${a-b}, Mul: ${a*b}, Div: ${a/b}, Mod: ${a%b}, Exp: ${a**b}`);
// let x = 5;
// console.log(x++); //Post increement prints the original first then increements
// console.log(++x); //Increements the original first then provides the updated result

////////////////////////Ques 10////////////////////////////

// Start with n = 100. Apply += 20, -= 10, *= 2, /= 4, %= 7, **= 2 one by one and print n after each. ☐ Expected: 120, 110, 220, 55, 6, 36

// let n = 100;
// console.log(n += 20, n-=10, n*= 2, n/= 4, n%= 7, n**= 2)

//////////////////////////Ques 11///////////////////////////////

// Print results of 5 == "5", 5 === "5", null == undefined, null === undefined, "10" > "9", 10 > 9 in a console.table with the expression and the result. 

// console.table([
//     { expression : `5 === "5"` , result : 5 === "5"},
//     { expression : `5 == "5` , result : 5 == "5"},
//     { expression : `null == undefined` , result : null === undefined},
//     { expression : `null == undefined` , result : null == undefined},
//     { expression : `"10" > "9"` , result : "10" > "9"},
//     { expression : `10 > 9` , result : 10 > 9},
// ])

///////////////////////////Ques 12/////////////////////////////

// Print "5" + 2, "5" - 2, 1 + 2 + "3". Then read two numbers using prompt() and print their correct numeric sum (not joined text). 

// let x = Number(prompt("Enter a number:"));
// let y = Number(prompt("Enter a number:"));
// const result = x + y;
// console.log(result)

// console.log("5" + 2);
// console.log("5" - 2);
// console.log(1 + 2 + "3");

/////////////////////////////Ques 13////////////////////

// Take marks as input. Print grade: >= 90 "A", >= 75 "B", >= 50 "C", else "Fail". Test with 95, 80, 55, 30. 

// let marks = prompt("Enter your marks:");
// if(marks>=90){
//     console.log("A")
// }
// else if (marks >= 75) {
//     console.log("B");
// }
// else if(marks >= 50) {
//     console.log("C");
// }
// else {
//     console.log("Fail")
// }

///////////////////////Ques 14//////////////////

// Using a ternary operator only, print whether a number is "Even" or "Odd", and whether age 20 "Can vote" or "Cannot vote". ☐

// let number = prompt("Enter a number:")
// let result = number % 2 === 0 ? "Even" : "Odd";
// console.log(result)

// let age = prompt("Enter your age:")
// let text = (age > 18) ? "Can Vote" : "Cannot Vote";
// console.log(text)

//////////////////////Ques 15///////////////////////////

// Using switch, print the day name for 1-7 with default. Then group cases so that 6 and 7 print "Weekend" and 1-5 print "Weekday". ☐

// let day = Number(prompt("Enter a number between 1 to 7 for day name:"))
// switch(day) {
//     case 1:
//         console.log("Sunday");
//         break;
    
//     case 2:
//         console.log("Monday");
//         break;

//     case 3:
//         console.log("Tuesday");
//         break; 

//     case 4:
//         console.log("Wednesday");
//         break;

//     case 5:
//         console.log("Thursday");
//         break;

//     case 6:
//         console.log("Friday");
//         break;
        
//     case 7:
//         console.log("Saturday");
//         break;
    
//     default:
//         console.log("Wrong Entry. Try again");
// }

// switch(day){
//     case 2:
//     case 3:
//     case 4:
//     case 5:
//     case 6:
//     console.log("Weekday");
//     break;

//     case 1:
//     case 7:
//     console.log("Weekend");
//     break;
// }

/////////////////////////////Ques 16/////////////////////////

// Write checkTruthy(value) that prints "truthy" or "falsy". Test with 0, "", null, undefined, NaN, [], {}, "0", "false". ☐ Expected falsy: 0, "", null, undefined, NaN. Truthy: [], {}, "0", "false".

// function checkTruthy(value) {
//     if (value){
//         console.log("truthy");
//     } else {
//         console.log("falsy");
//     }
// }

// checkTruthy(0);
// checkTruthy("");
// checkTruthy(null);
// checkTruthy(undefined);
// checkTruthy(NaN);
// checkTruthy([]);
// checkTruthy({});
// checkTruthy("0");
// checkTruthy("false");

///////////////////////////Ques 17//////////////////////////////

// Using ||, ?? and &&: set a username default to "Guest" when empty; show the difference between 0 || 10 and 0 ?? 10; call a function only if a flag is true using &&. ☐

// let input = "";
// let username = input || "Guest";
// console.log(username)

// console.log(0 || 10);
// console.log(0 ?? 10);
// console.log(0 && 10);

// let flag = true;
// function print() {
//     console.log("Hello JS");
// }
// flag && print();

///////////////////////////Ques 18//////////////////////////

// Using for, print numbers 1 to 10, their sum, and the multiplication table of 7 (up to 10). ☐ Expected sum: 55

// let sum = 0;
// let mul = 1

// for(let i = 1; i <= 10; i++){
//     console.log(i)
//     sum = sum + i
// }
// console.log("Total is",sum)

// for ( let j = 1; j <= 10; j++){
//     mul = 7 * j
//     console.log("7 times" ,j, "=", mul)
// }

/////////////////////Ques 19///////////////////////////

// Using while, find the sum of digits of 12345. Using do...while, show a loop with a false condition that still runs once. ☐ Expected: 15

// let digit = 12345
// let sum = 0
// while(digit > 0 ){
//     let last = digit % 10
//     sum += last
//     digit = Math.floor(digit / 10)
// }
// console.log(sum)

// let x = 10;
// do{
//     console.log("ok");
// } while (x <5)

///////////////////////Ques 20///////////////////////////

// Print 1 to 20, skip multiples of 3 using continue, and stop completely at 14 using break. ☐ Expected: 1,2,4,5,7,8,10,11,13

// for (let i = 1; i <= 20; i++){
//     if(i===14){
//         break;
//     }
//     if(i % 3 === 0){
//         continue;
//     }
//     console.log(i);

// }

////////////////////////Ques 21///////////////////////////////

// Loop through an array with for...of and through an object with for...in. Then print a star triangle of 5 rows using nested loops. ☐

// let fruits = ["apple","banana","grapes"];
// for(let fruit of fruits){
//     console.log(fruit)
// }

// let person = {
//     fname : "Dipesh",
//     lname : "Tambakhe",
//     age : 29
// }
// for(let name in person){
//     console.log(name + "=" + person[name])
// }

// for (let i = 1; i<= 5; i++){
//     let row = ""; 

//     for(let j=1; j<=i; j++){
//         row += "* "
//     }
//     console.log(row);
// }

//////////////////////////Ques 22///////////////////////////////

// Using template literals, print My name is Ravi and I am 22, a multi-line string and an expression like Total: ${10 + 5}. ☐

// let person = `
//  My name is Ravi 
//  and I am 22`;
//  console.log(person);
//console.log(`Total: ${10 + 5}`);

////////////////////////Ques 23/////////////////////////////////////

// For " Hello World " print: trimmed, upper case, lower case, World replaced by JS, length, split into array of words, and "5" padded to "005" using padStart. ☐

// let greet = " Hello World ";
// let i = greet.trim();
// console.log(i);

// console.log(i.toUpperCase());
// console.log(i.toLowerCase());
// console.log(i.replace("World","JS"));
// console.log(i.length);
// console.log(i.split(" "))

// let n = "5";
// let pad = n.padStart(3,"0");
// console.log(pad)

/////////////////////////////Ques 24/////////////////////////////////////

// Using slice, substring, substr extract "World" from "Hello World". Then print the initials of "Rahul Kumar Shah" as RKS. ☐

// let greet = "Hello World";
// let part = greet.slice(6);
// console.log(part);
// console.log(greet.substring(6));
// console.log(greet.substr(6));

// let name = "Rahul Kumar Singh";
// let words = name.split(" ");
// let initials = words[0][0] + words[1][0] + words[2][0];
// console.log(initials);

//////////////////////////////Ques 25///////////////////////////

// For "JavaScript is fun, JavaScript is powerful" print indexOf, lastIndexOf, includes("fun"), startsWith, endsWith and count how many times "JavaScript" appears. ☐ Expected count: 2

// let sentence = "JavaScript is fun, JavaScript is powerful";
// console.log(sentence.indexOf("fun"));
// console.log(sentence.lastIndexOf("powerful"));
// console.log(sentence.includes("fun"));
// console.log(sentence.startsWith("JavaScript"));
// console.log(sentence.endsWith("ful"));

// let count = 0
// for(let word of sentence.matchAll("JavaScript")) {
//     count += 1
// }
// console.log(count)

///////////////////////////Ques 26///////////////////////////////

// Write reverseString(str) and isPalindrome(str). Test with "hello" and "madam". 

// function reverseString(str) {
//     return str.split("").reverse().join("")
// }
// console.log(reverseString("Hello"));
// console.log(reverseString("madam"));

// function isPalindrome(str) {
//     let reversed = reverseString(str);
//     return str === reversed;

// }
// console.log(isPalindrome("Hello"));
// console.log(isPalindrome("madam"));

//////////////////////QUes 27////////////////////////

// Print (3.14159).toFixed(2), parseInt("42px"), parseFloat("3.5kg"), Number("abc"). Convert 255 to binary and hex using toString(). ☐ Expected: "3.14", 42, 3.5, NaN, "11111111", "ff"

// console.log((3.14159).toFixed(2));
// console.log(parseInt("42px"));
// console.log((parseFloat("3.5kg")));
// console.log(Number("abc"));

// let num = 255;
// console.log((num.toString(2)));
// console.log((num.toString(16)));

///////////////////////Ques 28/////////////////////////////////////////

// Print Number.MAX_SAFE_INTEGER, Number.EPSILON. Compare 0.1 + 0.2 === 0.3 and fix the comparison using EPSILON. Check Number.isInteger(5.0) and isFinite(1/0). ☐

// console.log(Number.MAX_SAFE_INTEGER);
// console.log(Number.EPSILON);
// console.log(0.1 + 0.2 === 0.3);

// console.log(Number.isInteger(5.0));
// console.log(Number.isFinite(1/0));


//////////////////////////////////Ques 29//////////////////////////

// Using BigInt, calculate and print the factorial of 25. ☐ Expected: 15511210043330985984000000n

// let fact = 1n;
// for (let i =1n; i<= 25n; i++){
//     fact *= i
// }
// console.log(fact)

/////////////////////////////////Ques 30//////////////////////////////////

// Using bitwise operators: write isEven(n) with &, multiply 5 by 8 using <<, and print 5 & 1, 5 | 1, 5 ^ 1, ~5. ☐ Expected: 1, 5, 4, -6

// function even(n) {
//     return (n & 1) === 0;
// }
// console.log(even(4));
// console.log(even(7));

// console.log(5 << 3);
// console.log(5 & 1);
// console.log(5 | 1);
// console.log(5 ^ 1);
// console.log(~5);


//////////////////////////Ques 31//////////////////////////////////

// For radius 7.5 print the area of a circle rounded to 2 decimals. For [3, 9, 2] print max, min. Print Math.round(4.5), Math.ceil(4.1), Math.floor(-4.1), Math.trunc(-4.9), Math.sqrt(144), Math.pow(2, 10). ☐

// let radius = 7.5;
// let area = Math.PI * radius * radius;
// console.log(area.toFixed(2));

// let arr = [3,9,2];
// console.log(Math.max(...arr));
// console.log(Math.min(...arr));
// console.log(Math.round(4.5));
// console.log(Math.ceil(4.1));
// console.log(Math.floor(-4.1));
// console.log(Math.trunc(-4.9));
// console.log(Math.sqrt(144));
// console.log(Math.pow(2,10));

///////////////////////////////Ques 32//////////////////////////

// Write getRandomInt(min, max) (inclusive). Call it 10 times. Create a dice roller and a random hex colour generator. 



////////////////////////////////Ques 33////////////////////////

// Write a regex to validate a 10-digit Indian mobile number starting with 6-9. Test with 3 valid and 3 invalid numbers. ☐

// let numb = /^[6-9]\d{9}$/;
// console.log(numb.test("990954321"));
// console.log(numb.test("712345689"));
// console.log(numb.test("600011111"));

// console.log(numb.test("7016148083"))
// console.log(numb.test("7123458974"));
// console.log(numb.test("8547865545"));

//////////////////////////////////Ques 34//////////////////////////

// Using regex: extract all numbers from "a1b22c333", replace multiple spaces with one space, do a case-insensitive global replace of "js" with "JavaScript", and validate a simple email. ☐ Expected extraction: ["1","22","333"]

// let str = "a1b22c333"
// let numbers = str.match(/\d+/g);
// console.log(numbers);

// let space = "Hello    World";
// console.log(space.replace(/\s+/g, " "));

// let str2 = "js"
// console.log(str2.replace(/js/gi,"JavaScript"));


/////////////////////////////////Ques 35/////////////////////////////////

// Write add as a function declaration and as a function expression. Call both before their definition and show that one works (hoisting) and the other throws an error (catch and print it). ☐

// console.log("Declaration:", add(5,3));

// function add(a,b) {
//     return a+b;
// }

// try{
//     console.log("Expression:", added(5,3));
// } catch (error) {
//     console.log("Error:", error.message);
// }

// const added = function (a,b){
//     return a+b;
// }

/////////////////////////////////////Ques 36//////////////////////////////////

// Write greet(name = "Guest") using a default parameter, and sum(...nums) using a rest parameter. Test sum(1,2,3,4,5). ☐ Expected: "Hello Guest", 15

// function greet(name = "Guest") {
//     console.log("Hello " + name);
// }

// greet();

// function sum(...nums) {
//     let total = 0;
//     for(let n of nums) {
//         total += n;
//     }
//     return total;
// }

// console.log(sum(1,2,3,4,5));

//////////////////////////////////Ques 37/////////////////////////////

// Write stats(arr) that returns an object { min, max, avg }. Test with [4, 8, 15, 16, 23, 42]. ☐

// function stats(arr) {
//     let min = Math.min(...arr);
//     let max = Math.max(...arr);
//     let sum = 0;
    
//     for (let num of arr) {
//         sum += num;
//     }
//     let avg = sum / arr.length;
//     return {min,max,avg};
// }
// console.log(stats([4, 8, 15, 16, 23, 42]));

///////////////////////////////////////Ques 38/////////////////////////////////

// Convert square, add and greet to arrow functions (one with implicit return, one with a single parameter without brackets). Use an arrow function inside map. ☐

// const square = x => x * x;
// console.log(square(5));

// const add = (a,b) => a+b;
// console.log(add(5,5));

// const greet = name => {
//     return `Welcome, ${name}`;
// }
// console.log(greet("Dipesh"));

// let numbs = [1,2,3,4];
// let squared = numbs.map(n=>n*2);
// console.log(squared);

////////////////////////////////////////Ques 39//////////////////////////

// Write largest() using the arguments object to find the max of any number of arguments. Also show pass-by-value (number) and pass-by-reference (object) by changing both inside a function. ☐

// function largest(){
//     let max = arguments[0];
//     for (let i = 1; i<arguments; i++){
//         if(arguments[i] > max){
//             max = arguments[i]
//         }
//     }
//     return max;
// }
// console.log("largest:",largest(12,45,78,10,2));

// function change(num,obj){
//     num = 100;
//     obj.name = "Dipesh";
// }

// let myNum = 10;
// let myObj = {name : "Dipesh"};

// change(myNum,myObj);
// console.log(myNum,myObj)

///////////////////////////////////////Ques 40///////////////////////////

// Print a countdown from 5 to 1 each second using setInterval, then print "Go!" and stop using clearInterval. Also show "Done" after 2 seconds using setTimeout. ☐

// let countdown = 5;
// let timer = setInterval(() => {
//     if(countdown > 0){
//         console.log(countdown);
//         countdown--;
//     } else {
//         console.log("Go!");
//         clearInterval(timer);
//     }
// },1000);

// setTimeout(() => {
//     console.log("Done");
// },2000);

/////////////////////////////////Ques 41///////////////////////////////////////

// Demonstrate global, function and block scope. Show a ReferenceError (catch it). Show the difference between var and let inside a loop with setTimeout (prints 3,3,3 vs 0,1,2). ☐

// let global = "Global"

// function scope() {
//     let inside = "Inside function";

//     if(true) {
//         let block = "Inside block";
//         console.log(global,"|",inside,"|",block)
//     }
//     try{
//         console.log(block);
//     } catch(err){
//         console.log("Error caught:",err.name,"-",err.message);
//     }
// }
// scope();

// for(var i = 0; i < 3; i++){
//     setTimeout(()=> console.log("Var:",i),100);
// }

// for(let j = 0; j<3; j++){
//     setTimeout(() => console.log("Let:",j),200);
// }

///////////////////////////////Ques 42////////////////////////////////////////

// Demonstrate hoisting: print a var before declaration (undefined) and a let before declaration (catch the error from the temporal dead zone). ☐

// console.log("Before declaration:",a);
// var a = 10;

// try{
//     console.log(b);
// } catch (err) {
//     console.log("Temporal dead Zone Error:",err.name, "-", err.message);
// }

///////////////////////////Ques 43///////////////////////////////

// With "use strict" show errors for an undeclared variable and a duplicate parameter name. Catch and print the messages. ☐

// "use strict"

// try{
//     num = 50;
// } catch (err) {
//     console.log("Undeclared:", err.name ,"-", err.message)
// }

// try {
//     name("function duplicate(a,a) {return a;}");
// } catch (err) {
//     console.log("Duplicate error:", err.name, "-", err.message);
// }

////////////////////////////////Ques 44//////////////////////////////////////////

// Create object car with brand, model, year and a method fullInfo() using this. Print fullInfo(). 

// const car = {
//     brand : "Toyota",
//     model : "Supra",
//     year : 2026,
//     fullInfo : function() {
//         return `${this.brand} ${this.model} ${this.year}`;
//     }
// };
// console.log(car.fullInfo());

/////////////////////////////Ques 45///////////////////////////////////////

// For a student object: read a property with dot and bracket, add, modify, delete a property, and check with in and hasOwnProperty. Print the object after each step. ☐

// let student = {
//     name: "Dipesh",
//     age: 29
// };

// console.log(student.name);
// console.log(student["age"]);

// student.city = "Surat";
// console.log("New:",student);

// student.age = 65;
// console.log("modified:",student);

// delete student.age;
// console.log("Deleted:",student);

// console.log(student.hasOwnProperty("name"));
// console.log("age" in student);

//////////////////////////////////////Ques 46//////////////////////////////////////

// For a product object print Object.keys, Object.values, Object.entries, JSON.stringify and loop with for...in. ☐

// const product = {
//     name : "car",
//     model : "SUV",
//     condition : "New",
//     year : 2027
// };

// console.log("keys:", Object.keys(product));
// console.log("Values:", Object.values(product));
// console.log("Entries:", Object.entries(product));
// console.log("JSON:", JSON.stringify(product));

// let details = ""
// for( let prod in product) {
//     details += product[prod] + " ";
// }
// console.log(details)

///////////////////////////////Ques 47/////////////////////////////////////////////

// Create constructor Person(name, age) with a method. Create 2 objects using new and add a property to only one of them. ☐

// function person(name,age,city) {
//     this.fullName = name;
//     this.age = age;
//     this.city = city;
// }
// const myself = new person("Dipesh T", 29 ,"Surat");
// const anime = new person("Jinwoo", 25, "Japan");
// console.log(myself)
// console.log(anime)

// anime.power = "Necromancer"
// console.log(anime)

////////////////////////////Ques 48/////////////////////////////////

// On [10, 20, 30] do push(40), pop(), shift(), unshift(5). Print the array after each. ☐

// const arr = [10,20,30];
// arr.push(40);
// console.log(arr);

// arr.pop();
// console.log(arr);

// arr.shift()
// console.log(arr);

// arr.unshift(5);
// console.log(arr);

///////////////////////////////////////Ques 49//////////////////////////////

// On [1,2,3,4,5,6]: remove 2 middle items with splice, insert 2 items using splice, take a part using slice, join with -, concatenate with another array and flatten [1,[2,[3]]] using flat(Infinity). ☐

// const arr = [1,2,3,4,5,6];
// const arr2 = [7,8,9,10];
// arr.splice(2,2);
// console.log("Splice remove:",arr);

// arr.splice(2,0,7,9);
// console.log("Splice add:", arr);

// const newArr = arr.slice(4);
// console.log("Slice:", newArr);

// console.log("Join:",arr.join(" -"));

// const joined = arr.concat(arr2);
// console.log("Concat:",joined);

// const flatten = [1,[2,[3]]];
// const result = flatten.flat(Infinity);
// console.log("Flatten:", result);

////////////////////////////////Ques 50///////////////////////////////////

// On [5, 12, 8, 130, 44] find the first number > 10 (find), its index (findIndex), and check includes(8). On an array of objects find a user by id. ☐ Expected: 12, 1, true

// const arr = [5,12,8,130,44];
// console.log(arr.find( n => n > 10));
// console.log(arr.findIndex(n => n > 10));
// console.log(arr.includes(8));

// const user = [
//     {name : "Dipesh", id : 32},
//     {name : "Karan", id : 2},
// ]
// let findUser = user.find(user => user.id === 2);
// console.log(findUser);

////////////////////////////////////Ques 51///////////////////////////

// Sort ["Banana","Apple","Mango"]. Sort [40,100,1,5] ascending and descending. Sort an array of student objects by marks. Reverse an array. ☐ Expected ascending: 1,5,40,100

// const fruits = ["Banana","Apple","Mango"];
// console.log(fruits.sort())

// const numb = [40,100,1,5];
// numb.sort(function(a,b) {return a-b});
// console.log(numb);

// console.log(numb.sort(function(a,b) {return b-a}));

// const students = [
//     {name : "Dipesh" , marks : 80},
//     {name : "Karan" , marks : 90}
// ];

// students.sort((a,b) => a.marks - b.marks);
// console.log(students)

///////////////////////////////Ques 52//////////////////////////////////

// On [1,2,3,4,5] print: squares using map, even numbers using filter, sum using reduce, forEach printing each, every (all > 0) and some (any > 4). ☐

// const arr = [1,2,3,4,5];
// console.log("Squares:", arr.map(n => n * n));
// console.log("Even:", arr.filter(n => n % 2 === 0));
// console.log("Sum:", arr.reduce((a,b) => a + b ));

// arr.forEach((n => console.log(n)));

// console.log(arr.every(n => n > 0));
// console.log(arr.some(n => n > 4));

/////////////////////////////Ques 53//////////////////////////////////////////

// Show that const arr = [] allows push. Create [1..10] using Array.from({length: 10}, ...). Copy an array using spread. Check Array.isArray. ☐

// const arr = [];
// arr.push("Fruits");
// console.log(arr);

// const num = [];
// let create = Array.from({length : 10}, (value,index) => index+1 )
// console.log(create)

// let original = [1, 2, 3, 4, 5];
// let copy = [...original];

// console.log("Original Array:", original);
// console.log("Copied Array:", copy);



// console.log(Array.isArray(original));
// console.log(Array.isArray(copy));
// console.log(Array.isArray("Hello"));

///////////////////////////////Ques 54////////////////////////////////////

// Create a Set, use add, has, delete, size. Remove duplicates from [1,2,2,3,3,3] using a Set. ☐ Expected: [1,2,3]

// const arr = new Set([1,2,2,3,3,3]);
// console.log(arr);
// console.log(arr.add(4));
// console.log(arr.has(3));
// arr.delete(4);
// console.log(arr);
// console.log(arr.size);

//////////////////////////////////////Ques 55////////////////////////////

// For A = {1,2,3} and B = {2,3,4} print union, intersection and difference. ☐ Expected: {1,2,3,4}, {2,3}, {1}

// const A = new Set([1,2,3]);
// const B = new Set([2,3,4]);
// console.log(A.union(B));
// console.log(A.intersection(B));
// console.log(A.difference(B));

//////////////////////////////Ques 56//////////////////////////////

// Create a phonebook Map with 3 entries. Use set, get, has, delete, size and loop with for...of and forEach. 

// const phonebook = new Map([
//     ["Dipesh", 8756339758],
//     ["Karan",5784656738],
//     ["Dev", 8644587897]
// ]);

// console.log(phonebook.set("Dev", 1234567890));
// console.log(phonebook.get("Dipesh"));
// console.log(phonebook.has("Dev"));
// console.log(phonebook.delete("Dev"));
// console.log(phonebook.size);

// for (let [name,numb] of phonebook){
//     console.log(`${name} : ${numb}` )
// }

// phonebook.forEach(function(a,b){
//     console.log(`${a} : ${b}`);
// })

/////////////////////////////////// Ques 57 ///////////////////////////////

// Count the frequency of each word in "the cat and the hat and the bat" using a Map. Also use a WeakSet to track visited objects. ☐ Expected: the=3, and=2


// let str = "the cat and the hat and the bat";
// let words = str.split(" ");
// let freq = new Map();

// for (let word of words) {
//     freq.set(word, (freq.get(word) || 0) + 1);
// }


// for (let [word, count] of freq) {
//     console.log(word + " = " + count);
// }



// let visited = new WeakSet();
// let obj1 = { name: "Rahul" };
// let obj2 = { name: "Amit" };

// visited.add(obj1);
// visited.add(obj2);

// console.log("obj1 visited:", visited.has(obj1));
// console.log("obj2 visited:", visited.has(obj2));

// let obj3 = { name: "Raj" };

// console.log("obj3 visited:", visited.has(obj3));


////////////////////////////////////// Ques 58 ///////////////////////

// Loop through a string, array, Set and Map using for...of. Spread a string into an array and convert a Map into an array using Array.from. ☐

// let str = "Hello World";
// for(i of str){
//     console.log(i)
// }

// let arr = [1,2,3,4,5];
// for(j of arr){
//     console.log(j)
// }

// let mySet = new Set([1,1,2,3,4,4,4,5]);
// for(k of mySet){
//     console.log(k);
// }

// let myMap = new Map([
//     ["a" , 1],
//     ["b" , 2]]);

// for(l of myMap){
//     console.log(l)
// }

// const arr2 = [...arr, ...str];
// console.log(arr2);

// console.log(Array.from(myMap));

//////////////////////////// Ques 59 ///////////////////////////////////////

// Create a custom iterator object (using Symbol.iterator) for numbers 1 to 5, and a generator fibonacci() that prints the first 10 Fibonacci numbers using .next(). ☐ Expected: 0,1,1,2,3,5,8,13,21,34




///////////////////////////// Ques 60 ////////////////////////////////////////

// Print today's date as DD-MM-YYYY, the weekday name, and create the date 15 Jan 2026 with year, month, day. ☐

// let today = new Date();
// console.log(today)

// const days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
// const d = new Date("2026-04-22");
// let day = days[d.getDay()];
// console.log(day);

/////////////////////////////////// Ques 61 //////////////////////////////////////

// Add 7 days to today using setDate, and calculate the number of days between today and 31 Dec of this year. ☐

// const today = new Date();
// today.setDate(today.getDate() + 7);
// console.log(today)

/////////////////////////////// Ques 62 //////////////////////////////////////////

// Print a console.table of typeof for: null, [], {}, function(){}, NaN, undefined, 10n, Symbol(), "a", new Date(). ☐ Expected: object, object, object, function, number, undefined, bigint, symbol, string, object

// let table = [
//     {value : "null", type : typeof null},
//     {value : "[]", type : typeof []},
//     {value : "{}", type : typeof {}},
//     {value : "function", type : typeof function(){}},
//     {value : "NaN", type : typeof NaN},
//     {value : "undefined", type : typeof undefined},
//     {value : "10n", type : typeof 10n},
//     {value : "Symbol", type : typeof Symbol()},
//     {value : "a", type : typeof "a"},
//     {value : "Date", type : typeof new Date}
// ]
// console.log(table)

////////////////////////////////// Ques 63 ////////////////////////////////////////

// Show a function returning undefined, reading a missing property, using ?. and ??. Check NaN correctly using Number.isNaN and show NaN === NaN. ☐

// function undefine() {
//     let x = 5;
// }
// console.log(undefine());

// let user = { name : "Dipesh"};
// console.log(user.age);
// console.log(user.address?.city);
// console.log(user.age?? 18);

// console.log(NaN===NaN);
// console.log(Number.isNaN(NaN));

////////////////////////////////////////// Ques 64 //////////////////////////////////

// For ["5", "abc", "", true, null, undefined, "0"] print Number(), String(), Boolean() results in a console.table. Print "3"+4+5 and 3+4+"5". ☐

// let arr = ["5", "abc", "", true, null, undefined, "0"];
// let table = arr.map(val => ({
//     Input : String(val),
//     Number : Number(val),
//     String : String(val),
//     Boolean : Boolean(val)

// }));
// console.log(table)

// console.log("3" + 4 + 5);
// console.log(3 + 4 + "5");


////////////////////////////////// Ques 65 //////////////////////////////////////

// Using destructuring: array with skipping, object with a default value and rename, nested object, function parameter destructuring. Swap a and b without a temp variable. ☐



///////////////////////////////// Ques 66 ///////////////////////////////////////

// Create an object with a Symbol("id") key and show it is hidden from Object.keys. Format 1234567.89 using toLocaleString("en-IN") and as INR currency. ☐ Expected: "12,34,567.89"

// let id = Symbol("id");

// let student = {
//     name: "Rahul",
//     age: 20,
//     [id]: 101
// };

// console.log(student);
// console.log(Object.keys(student));
// console.log(student[id]);

// let num = 1234567.89;

// console.log(num.toLocaleString("en-IN"));
// console.log(num.toLocaleString("en-IN", {
//     style: "currency",
//     currency: "INR"
// }));

///////////////////////////////// Ques 67 ////////////////////////////////////////////////////

// Use try...catch...finally to parse an invalid JSON string. Print the error message in catch and "Done" in finally. ☐

// let details = `{name : "Dipesh}`

// try {
//     let data = JSON.parse(details);
//     console.log(data);
// } catch (err) {
//     console.log(err.name , err.message);
// } finally {
//     console.log("Done");
// }

///////////////////////////////////Ques 68///////////////////////////////

// Write setAge(age) that throws a custom error when age is negative or not a number. Trigger and catch a ReferenceError, TypeError and SyntaxError; print error.name and error.message for each. ☐

// function setAge(age) {
//     if ( age !== "number" || age < 0) {
//         throw new Error("Age must be a non-negative number.");
//     }
//     console.log(age);
// }

// try {
//     setAge(-5);
// } catch (error) {
//     console.log(error.name + ": " + error.message);
// }

// try {
//     console.log(undefinedVariable);
// } catch (error) {
//     console.log(error.name + ": " + error.message);
// }

// try {
//     let num = null;
//     num.toString();
// } catch (error) {
//     console.log(error.name + ": " + error.message);
// }

// try {
//     eval("let x = ;");
// } catch (error) {
//     console.log(error.name + ": " + error.message);
// }

///////////////////////////////// Ques 69 ////////////////////////////////

// Use console.error, console.warn, console.table, console.time to measure a loop of 1,000,000 iterations. Add a debugger statement and pause at it in DevTools. ☐

// console.error("Error message");
// console.warn("Warning");
// console.table([{ id : 1, status : "Active"}]);
// console.time("Loop Timer");

// let total = 0;
// for(let i = 0; i < 1000000; i++){
//     total += i;
// }
// console.timeEnd("Loop Timer");

// debugger;
// console.log("Finished");

///////////////////////////////// Ques 70 ////////////////////////////////////

// Fix the bugs in this code and show the correct output. Also set a breakpoint in DevTools and show the value of sum in Watch. ☐

// function total(prices) {
//   let sum = 0;                // Intialised sum to sum = 0
//   for (let i = 0; i < prices.length; i++) {           //i < prices instead of i <= prices
//     sum += prices[i];
//   }
//   return sum;
// }
// console.log(total([10, 20, 30])); // Output 60

///////////////////////////////////// Ques 71 ////////////////////////////////

// Rewrite this code to follow the style guide (camelCase names, spacing, indentation, semicolons, const/let, no global leaks): ☐

// let totalPrice = 0;
// function calcTotal(price,qty) {
//     const totalPrice = price * qty; 

// return totalPrice;
// }

///////////////////////////////// Ques 72 //////////////////////////////////////////

// Fix these 4 common mistakes so the code prints the expected result: ☐

// let x = 3;
// if (x === 5) { 
//     console.log("x is five"); 
// }           // should print nothing (x is 3)

// console.log(Number((0.1 + 0.2).toFixed(1)) === 0.3);                    // should print true (use a fix)

// function getValue() {
//   return 42;
// }
// console.log(getValue());                           // should print 42

// switch (1) { 
//     case 1: 
//     console.log("one"); 
//     break;

//     case 2: 
//     console.log("two");
//     break; 
// }  // should print only "one"

///////////////////////////////  Ques 84 ////////////////////////////////

// Create a JSON string of 3 students (name, marks array). Parse it and print each student's average marks. ☐

// let students = '[{"name" : "Dipesh" , "marks" : [85,79]} , {"name" : "Ravi Kishan" , "marks" : [89,90]} , {"name" : "Hulku re" , "marks" : [99,89]} ]'

// let marks = JSON.parse(students);

// for(let i = 0; i < marks.length; i++) {
//     let sum = 0;

//     for(let j = 0; j < marks[i].marks.length; j++) {
//         sum += marks[i].marks[j];
//     }

//     console.log(marks[i].name + ": " + sum / marks[i].marks.length);
// }

//////////////////////////////// Ques 85 /////////////////////////////

// Use JSON.stringify with spacing (pretty print) and a replacer to hide a password field. Clone an object using JSON.parse(JSON.stringify(obj)). ☐

// let details = {
//     name : "Dipesh",
//     email : "d@123.com",
//     password : 122445677890
// }

// let str = JSON.stringify(details, function(key,value){
//     if (key === "password"){
//         return undefined;
//     }
//     return value;
// },2);

// console.log(str);

// let data = JSON.stringify(details);
// let clone = JSON.parse(data);
// console.log(clone);

/////////////////////////// Ques 87 ////////////////////////////////////////

// Write one program using ES6 features (let/const, arrow, template literal, destructuring, spread, default parameter) and one using newer features (?., ??, at(), Object.fromEntries, flat()). ☐

//////////// Program 1 ///////////////

// const name = "Dipesh";
// let total = 0;

// const itemTotal = (price,qty) => price * qty;
// price = prompt("Enter price: ");
// qty = prompt("Enter qty: ");
// total += itemTotal(price,qty);

// const customer = {
//     custName : "Hulku",
//     custId : 7,
//     city : "surat"
// };

// const {custName , custId, city} = customer;
// const message = `Hello ${custName}, your total is ${total}`;
// console.log(message);

// const cart = ["bread","cake","pastry"];
// let newItem = "";

// if(confirm("Want to add new item?")){
//     newItem = prompt("Add new item");
//     const newCart = [...cart,newItem];

//         if(newItem){
//             let newPrice = Number(prompt("Enter the price of new item"));
//             let newQty = Number(prompt("Enter qty of new item"));
//             total += newPrice * newQty;
//             console.log(`Your new total is ${total}`);
//         }
//     console.log(`You have added new items: ${newCart}`);
// } else {
//     console.log(`Final Items: ${cart}`);
// }

// const finalBill = (amount,discount = 10) => {
//     let semi = amount * discount / 100;
//     return amount -= semi;
// }

// console.log(`Hello ${custName}, your final bill is ${finalBill(total)}`);

////////////////// Program 2/////////////////////

// const customer = {
//     name : "Ayesha",
//     orders : [["bread",50] , ["coke", 90]]
// };

// const customer2 = {
//     name : "Anisha",
//     address : {
//         city : "Surat"
//     }
// }

// console.log(customer.address?.city);
// console.log(customer2.address.city);

// console.log(customer.address?.city ?? "Bhandup");

// console.log(customer.orders.at(-1));
// console.log(customer.orders.at(-1).at(0));

// let flatten = customer.orders.flat();
// console.log(flatten);

// let entries = Object.fromEntries(customer.orders);
// console.log(entries);



////////////////////////// Ques 88 //////////////////////////////////

// Callbacks and Closures: Write calculator(a, b, callback) that works with add and multiply callbacks. Write createCounter() using a closure so the count cannot be changed from outside. ☐

// function add(a,b) {
//     return a+b
// }

// function multiply(a,b) {
//     return a*b
// }

// function calculator(a,b,callback) {
//     return callback(a,b)
// }

// console.log(calculator(2,2,add));
// console.log(calculator(2,5,multiply));

// function createCounter(){
//     let counter = 0;
//     return count

//     function count(){
//         return counter += 1
//     }
// }

// const c = createCounter()
// console.log(c());
// console.log(c());
// console.log(c());

//////////////////////// Ques 89 ///////////////////////////

// Call, Apply, Bind: Using person1.fullName, print the full name of person2 using call(), apply() and bind(). ☐

// let person1 = {
//     fullName : "Dipesh T",
//     print : function(city,state){
//         console.log(this.fullName,city,state);
//     }
// }
// person1.print();

// let person2 = {
//     fullName : "Hulku Re"
// }
// person1.print.call(person2);
// person1.print.apply(person2,["Surat","Gujarat"]);

// let joint = person1.print.bind(person2,"Surat","Gujarat");
// joint()


//////////////////////////// Ques 90 ////////////////////////////

// Prototypes, Get/Set, Protection: Add a method greet through Person.prototype. Create an object with a getter and setter. Use Object.freeze() and show that changes are ignored. ☐

// function Person(name) {
//     this.name = name;
// }

// let details = new Person("Dipesh");

// Person.prototype.greet = function() {
//     console.log(`Hello, my name is ${this.name}`);
// };

// details.greet();

// let student = {
//     _name : "Rahul",
//     get name() {
//         return this._name;
//     },
//     set name(newName) {
//         if (typeof newName === "string" && newName.length > 0) { 
//             this._name = newName;
//         }
//     }
// };
// student.name = "Lara Dutta";
// console.log(student.name)

// Object.freeze(student);

// student.name = "Raj";
// console.log(student.name);


function BankAccount(owner,balance) {
    this.owner = owner;
    this._balance = balance;
}
let acc = new BankAccount("Dipesh", 1000)

BankAccount.prototype.deposit = function(amount) {
    this._balance += amount;
    console.log(`Your balance is ${this._balance}`)
};

acc.deposit(1000);

Object.defineProperty(BankAccount.prototype, "balance" , {
    get: function() {
        return this._balance;
    },
    set: function(balance) {
        if (balance > 0) {
            this._balance = balance;
        }
    }
});

acc.balance = 5000;
console.log(acc.balance)

function createCounter() {
    let count = 0;
    return createCounter;
}

//////////////////// Ques 91 ///////////////////////////

