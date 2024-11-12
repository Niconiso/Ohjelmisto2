function karkausvuosi() {
    const year = parseInt(prompt("Enter a year:"));
    let karkausvuosi = false;

    if (year % 4 === 0) {
        if (year % 100 === 0) {
            if (year % 400 === 0) {
                karkausvuosi = true;
            }
        } else {
            karkausvuosi = true;
        }
    }
    if (karkausvuosi) {
        document.write(year + " on karkausvuosi");
    } else {
        document.write(year + " ei ole karkausvuosi");
    }
}