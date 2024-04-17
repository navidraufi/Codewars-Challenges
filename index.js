num = [2, 5, 6, 8, 10, 0];

// function findOutlier(integers) {
//   var outlierOdd = {
//     value: null,
//     amount: 0,
//   };
//   var outlierEven = {
//     value: null,
//     amount: 0,
//   };

//   for (const i of integers) {
//     if (i % 2 !== 0) {
//       outlierOdd.amount++;
//       outlierOdd.value = i;
//     }

//     if (i % 2 === 0) {
//       outlierEven.amount++;
//       outlierEven.value = i;
//     }
//   }

//   if (outlierEven.amount > 1) {
//     return outlierOdd.value;
//   } else if (outlierOdd.amount > 1) {
//     return outlierEven.value;
//   }
// }

// function findOutlier(int) {
//   var even = int.filter((a) => a % 2 == 0);
//   var odd = int.filter((a) => a % 2 !== 0);
//   return even.length == 1 ? even[0] : odd[0];
// }

// function validatePIN(pin) {
//   if (typeof pin !== "string" || pin.length === 0) {
//     return false;
//   }
//   if (pin.length === 4 || pin.length === 6) {
//     var digitRegex = /^\d+$/;

//     if (digitRegex.test(pin)) {
//       return true;
//     } else {
//       return false;
//     }
//   } else {
//     return false;
//   }
// }

// function validatePIN(pin) {
//   return /^(\d{4}|\d{6})$/.test(pin);
// }

// function boolToWord(bool) {
//   return bool ? "Yes" : "No";
// }

// function descendingOrder(n) {
//   //   let digitArray = n.toString().split("");
//   //   digitArray.sort((a, b) => b - a);
//   //   return parseInt(digitArray.join(""));

//   return parseInt(String(n).split("").sort().reverse().join(""));
// }

// function solution(str) {
//   return str.split("").reverse().join("");
// }

// console.log(solution("Hello"));

// toCamelCase;

// function toCamelCase(str) {
//   let separator = str.includes("-") ? "-" : "_";

//   let ifHasBoth = str.includes("-") && str.includes("_");

//   if (!ifHasBoth) {
//     let splitArray = str.split(separator);

//     let capitalizedWords = splitArray.map((word, index) => {
//       if (index !== 0) {
//         return word.charAt(0).toUpperCase() + word.slice(1);
//       } else {
//         return word;
//       }
//     });
//     return capitalizedWords.join("");
//   } else {
//     return toCamelCase(capitalizedWords.join(""));
//   }
// }

// console.log(toCamelCase("The_cat-Is-Pippi"));

// function areYouPlayingBanjo(name) {
//   return name.toLowerCase()[0] === "r"
//     ? `${name} plays banjo`
//     : `${name} does not play banjo`;
// }

// console.log(areYouPlayingBanjo("Raufi"));

// String.prototype.toJadenCase = function () {
//   return this.split(" ")
//     .map((e) => e[0].toUpperCase() + e.slice(1))
//     .join(" ");
// };

// console.log("How can mirrors be real if our eyes aren't real".toJadenCase());

// function squareDigits(num) {
//   return Number(
//     String(num)
//       .split("")
//       .map((e) => Number(e) ** 2)
//       .map((i) => String(i))
//       .join("")
//   );
// }

// console.log(squareDigits(520));

// function getCount(str) {
//   let vowels = ["a", "e", "i", "o", "u"];

//   let count = 0;

//   function countLetter(word, letter) {
//     let count = 0;
//     for (let i = 0; i < word.length; i++) {
//       if (word[i] === letter) {
//         count++;
//       }
//     }
//     return count;
//   }

//   for (i of vowels) {
//     count += countLetter(str, i);
//   }

//   return count
// }

// console.log(getCount("Hello World"));
