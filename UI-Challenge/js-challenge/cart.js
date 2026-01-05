
function startBilling() {

    /*************************************************
     * UTILITY FUNCTIONS (VALIDATION HELPERS)
     *************************************************/
    function getNonEmptyString(message) {
        let value;
        do {
            value = prompt(message);
            if (!value || value.trim() === "") {
                alert("This field cannot be empty.");
            }
        } while (!value || value.trim() === "");
        return value.trim();
    }

    function getPositiveNumber(message) {
        let num;
        do {
            num = Number(prompt(message));
            if (isNaN(num) || num <= 0) {
                alert("Please enter a valid number greater than 0.");
            }
        } while (isNaN(num) || num <= 0);
        return num;
    }

    function validateEmail(email) {
        return /^[a-zA-Z0-9._%+-]+@karunya\.edu$/.test(email);
    }

    /*************************************************
     * LAB 1: ADD ITEMS TO CART
     *************************************************/
    let cart = [];

    while (true) {
        let itemCode = getNonEmptyString("Enter Item Code (e.g., A101)");
        let description = getNonEmptyString("Enter Item Description");
        let quantity = getPositiveNumber("Enter Quantity");
        let pricePerUnit = getPositiveNumber("Enter Price per Unit");

        cart.push({
            itemCode,
            description,
            quantity,
            pricePerUnit,
            totalPrice: quantity * pricePerUnit
        });

        let more = prompt("Do you want to add another item? (yes/no)").toLowerCase();
        if (more !== "yes") break;
    }

    if (cart.length === 0) {
        alert("Cart cannot be empty. Billing stopped.");
        return;
    }

    let subTotal = cart.reduce((sum, item) => sum + item.totalPrice, 0);

    /*************************************************
     * LAB 2 & 10: MEMBERSHIP DISCOUNT (WITH CLOSURE)
     *************************************************/
    function getDiscountFunction(type) {
        let rate =
            type === "Silver" ? 0.05 :
            type === "Gold" ? 0.10 :
            type === "Platinum" ? 0.15 : 0;

        return amount => amount * rate;
    }

    let membershipType;
    do {
        membershipType = prompt(
            "Enter Membership Type:\nNone / Silver / Gold / Platinum"
        );
    } while (!["None", "Silver", "Gold", "Platinum"].includes(membershipType));

    let discountFn = getDiscountFunction(membershipType);
    let discountAmount = discountFn(subTotal);
    let discountedTotal = subTotal - discountAmount;

    /*************************************************
     * LAB 3: GST & PLATFORM FEE
     *************************************************/
    const GST_RATE = 0.18;
    const PLATFORM_FEE_RATE = 0.002;

    let gstAmount = discountedTotal * GST_RATE;
    let platformFee = discountedTotal * PLATFORM_FEE_RATE;
    let totalWithTax = discountedTotal + gstAmount + platformFee;

    /*************************************************
     * LAB 4: PAYMENT MODE CHARGES
     *************************************************/
    let paymentMode;
    do {
        paymentMode = prompt("Payment Mode (Card / UPI / Cash)");
    } while (!["Card", "UPI", "Cash"].includes(paymentMode));

    let surcharge = 0;
    let convenienceFee = 0;

    if (paymentMode === "Card" && totalWithTax < 1000) {
        surcharge = totalWithTax * 0.025;
    } else {
        convenienceFee = totalWithTax * 0.01;
    }

    let finalAmount = totalWithTax + surcharge + convenienceFee;

    /*************************************************
     * LAB 11: ASYNC PAYMENT SIMULATION
     *************************************************/
    async function processPayment() {
        alert("Processing payment... Please wait");
        await new Promise(resolve => setTimeout(resolve, 2000));
        return true;
    }

    /*************************************************
     * LAB 6 & 8: EMAIL VALIDATION
     *************************************************/
    let email;
    do {
        email = prompt("Enter Email ID (must end with @karunya.edu)");
        if (!validateEmail(email)) {
            alert("Invalid email. Please use @karunya.edu domain.");
        }
    } while (!validateEmail(email));

    /*************************************************
     * LAB 5: FINAL INVOICE DISPLAY
     *************************************************/
    processPayment().then(() => {

        let invoiceNumber = "INV" + Math.floor(Math.random() * 100000);
        let invoiceDate = new Date().toLocaleString();

        console.clear();
        console.log("🧾 KARAZON.COM - FINAL INVOICE");
        console.log("Invoice No:", invoiceNumber);
        console.log("Invoice Date:", invoiceDate);
        console.log("Customer Email:", email);
        console.log("------------------------------------------------");

        console.table(cart);

        console.log("------------------------------------------------");
        console.log("Subtotal            :", subTotal.toFixed(2));
        console.log("Membership Discount :", discountAmount.toFixed(2));
        console.log("GST (18%)           :", gstAmount.toFixed(2));
        console.log("Platform Fee        :", platformFee.toFixed(2));
        console.log("Payment Charges     :", (surcharge + convenienceFee).toFixed(2));
        console.log("------------------------------------------------");
        console.log("FINAL AMOUNT PAYABLE:", finalAmount.toFixed(2));
        console.log("------------------------------------------------");
        console.log("✅ Payment Successful");
        console.log("📧 Invoice sent to", email);
        console.log("🙏 Thank you for shopping with Karazon.com");

        /*************************************************
         * LAB 7: SAVE TO LOCAL STORAGE
         *************************************************/
        localStorage.setItem("karazonInvoice", JSON.stringify({
            invoiceNumber,
            invoiceDate,
            cart,
            finalAmount,
            email
        }));
    });
}
