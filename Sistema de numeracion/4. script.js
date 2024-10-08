// Función para convertir de hexadecimal a decimal
function hexToDecimal(hex) {
    return parseInt(hex, 16);
}

// Función para convertir de decimal a hexadecimal
function decimalToHex(decimal) {
    return decimal.toString(16).toUpperCase();
}

// Función para convertir de BCD a decimal
function bcdToDecimal(bcd) {
    var decimal = 0;
    for (var i = 0; i < bcd.length; i++) {
        decimal = decimal * 100 + (bcd[i] >> 4) * 10 + (bcd[i] & 0x0F);
    }
    return decimal;
}

// Función para convertir de decimal a BCD
function decimalToBCD(decimal) {
    var bcd = [];
    while (decimal > 0) {
        var digit = decimal % 10;
        bcd.unshift((digit >> 4) * 16 + (digit & 0x0F));
        decimal = Math.floor(decimal / 10);
    }
    return bcd;
}

// Función para convertir de octal a decimal
function octalToDecimal(octal) {
    return parseInt(octal, 8);
}

// Función para convertir de decimal a octal
function decimalToOctal(decimal) {
    return decimal.toString(8);
}

// Función para determinar el tipo de entrada y realizar la conversión adecuada
function convertNumber(input) {
    var result = {};

    if (!isNaN(input)) {
        var decimal = parseInt(input);

        result.decimal = decimal;
        result.hexadecimal = decimalToHex(decimal);
        result.octal = decimalToOctal(decimal);
        result.bcd = decimalToBCD(decimal);
        result.bcdDecimal = bcdToDecimal(result.bcd);
    } else if (/^0x[0-9A-Fa-f]+$/.test(input)) {
        var hex = input.slice(2);

        result.hexadecimal = hex.toUpperCase();
        result.decimal = hexToDecimal(hex);
        result.octal = decimalToOctal(result.decimal);
        result.bcd = decimalToBCD(result.decimal);
        result.bcdDecimal = bcdToDecimal(result.bcd);
    } else if (/^[0-7]+$/.test(input)) {
        result.octal = input;
        result.decimal = octalToDecimal(input);
        result.hexadecimal = decimalToHex(result.decimal);
        result.bcd = decimalToBCD(result.decimal);
        result.bcdDecimal = bcdToDecimal(result.bcd);
    } else {
        result.error = "Entrada no válida";
    }

    return result;
}

// Ejemplo de uso
var inputNumber = ""; // Ingresa aquí el número que desees convertir
var conversionResult = convertNumber(inputNumber);
console.log("Resultado de la conversión:", conversionResult);
