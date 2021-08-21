function convertToRoman(num) {
  let decimalArr = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
  let romanArr = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V" ,"IV", "I"];
  var roman = "";

  for(var i=0 ; i<decimalArr.length ; i++) {
    while(decimalArr[i] <= num) {
      roman += romanArr[i];
      num -= decimalArr[i];
    }
  }
  return roman;
}

convertToRoman(36);