function laskuri() {
  const num1 = (prompt("Anna ensimmäinen numero:"));
  const num2 = (prompt("Anna toinen numero:"));
  const num3 = (prompt("Anna kolmas numero:"));
  const sum = num1 + num2 + num3;
  const product = num1 * num2 * num3;
  const average = (num1 + num2 + num3) / 3;
  console.log("Sum:", sum);
  console.log("Product:", product);
  console.log("Average:", average);
}