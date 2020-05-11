// temperature converter javascript

function convertTemp(celcius) {
   var farenheit = (celcius * 9/5) + 32;
   return farenheit;
   }

console.log(convertTemp(21.5));
console.log(convertTemp(-7));
console.log("Your converted value of 11 is " + convertTemp(11));
console.log(convertTemp(0));


