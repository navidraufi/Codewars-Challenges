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
