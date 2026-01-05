// /* ================= LAB 9: Custom Validation Error ================= */
// class ValidationError extends Error {
//   constructor(message) {
//     super(message);
//     this.name = "ValidationError";
//   }
// }

// /* ================= LAB 10: Closure-based Discount ================= */
// function getDiscountFunction(type) {
//   const rates = {
//     silver: 0.05,
//     gold: 0.10,
//     platinum: 0.15,
//     none: 0
//   };
//   return function(baseAmount) {
//     const rate = rates[type.toLowerCase()] ?? 0;
//     return {
//       discountRate: rate,
//       discountAmount: baseAmount * rate,
//       discountedTotal: baseAmount - baseAmount * rate
//     };
//   };
// }

// /* ================= LAB 12: Inventory Check (Skip if stock insufficient) ================= */
// async function validateAndAddItem(item) {
//   return new Promise((resolve) => {
//     const inventory = {
//       "ITEM1": 10,
//       "ITEM2": 5,
//       "ITEM3": 20
//     };
//     let stock = inventory[item.itemCode.toUpperCase()] ?? 0;
//     if (item.quantity <= stock) {
//       resolve(true); // Item OK, add to cart
//     } else {
//       alert(`Insufficient stock for ${item.itemCode}. Skipping this item.`);
//       resolve(false); // Skip item
//     }
//   });
// }

// /* ================= LAB 11: Async Payment ================= */
// async function processPayment(finalAmount, paymentMode) {
//   console.log(`Processing ${paymentMode} payment for ₹${finalAmount.toFixed(2)}...`);
//   return new Promise((resolve) => {
//     setTimeout(() => {
//       console.log("Payment confirmed ✅");
//       resolve({ status: "success", mode: paymentMode, amount: finalAmount });
//     }, 2000);
//   });
// }

// /* ================= LAB 13: Callback for Billing Completion ================= */
// function completeBilling(callback, invoiceData) {
//   callback(invoiceData);
// }

// /* ================= MAIN FLOW ================= */
// (async function main() {
//   try {
//     /* ===== LAB 7: Persistent Cart ===== */
//     let previousInvoice = localStorage.getItem("karazon_invoice");
//     let cart = [];
//     let subtotal = 0;

//     if (previousInvoice) {
//       let resume = confirm("Previous cart found. Resume previous cart?");
//       if (resume) {
//         previousInvoice = JSON.parse(previousInvoice);
//         cart = previousInvoice.cart;
//         subtotal = previousInvoice.subtotal;
//         console.log("Previous cart loaded:", cart);
//       }
//     }

//     /* ===== LAB 1: Add Items ===== */
//     let addMore = true;
//     while (addMore) {
//       let itemCode = prompt("Enter item code (e.g., ITEM1):");
//       let description = prompt("Enter item description:");
//       let quantity = Number(prompt("Enter quantity:"));
//       if (isNaN(quantity) || quantity <= 0)
//         throw new ValidationError("Quantity must be greater than 0");

//       let price = Number(prompt("Enter price per unit:"));
//       if (isNaN(price) || price <= 0)
//         throw new ValidationError("Price must be greater than 0");

//       let item = { itemCode, description, quantity, price, total: quantity * price };

//       /* ===== LAB 12: Inventory Lookup ===== */
//       const valid = await validateAndAddItem(item);
//       if (valid) {
//         cart.push(item);
//         subtotal = cart.reduce((s, i) => s + i.total, 0);
//       }

//       addMore = prompt("Add another item? (yes/no)").toLowerCase() === "yes";
//     }

//     if (cart.length === 0)
//       throw new ValidationError("Cart cannot be empty");

//     /* ===== LAB 10: Membership Discount ===== */
//     let membershipType = "none";
//     if (prompt("Are you a member? (yes/no)").toLowerCase() === "yes") {
//       membershipType = prompt("Membership type (Silver/Gold/Platinum):");
//     }

//     const discountFn = getDiscountFunction(membershipType);
//     const discountInfo = discountFn(subtotal);

//     /* ===== LAB 3: GST & Platform Fee ===== */
//     const gst = discountInfo.discountedTotal * 0.18;
//     const platformFee = discountInfo.discountedTotal * 0.002;
//     let totalWithTax = discountInfo.discountedTotal + gst + platformFee;

//     /* ===== LAB 4: Payment Mode ===== */
//     let paymentMode = prompt("Payment mode (Card/UPI/Cash):").toLowerCase();
//     if (!paymentMode)
//       throw new ValidationError("Payment mode cannot be empty");

//     let surcharge = 0;
//     let convenienceFee = 0;

//     if (paymentMode === "card" && totalWithTax < 1000)
//       surcharge = totalWithTax * 0.025;
//     else if (paymentMode !== "card")
//       convenienceFee = totalWithTax * 0.01;

//     let finalAmount = totalWithTax + surcharge + convenienceFee;

//     /* ===== LAB 11: Async Payment Confirmation ===== */
//     const paymentResult = await processPayment(finalAmount, paymentMode);

//     /* ===== LAB 8: Email Validation & Notification ===== */
//     const emailRegex = /^[a-zA-Z0-9._%+-]+@karunya\.edu$/;
//     let email = prompt("Enter email (@karunya.edu):");
//     while (!emailRegex.test(email)) {
//       alert("Invalid email format");
//       email = prompt("Enter valid email (@karunya.edu):");
//     }
//     console.log(`Invoice confirmation sent to ${email}`);

//     /* ===== LAB 5 & 6: Invoice Generation & Local Save ===== */
//     let invoice = {
//       invoiceNo: "INV-" + Math.floor(Math.random() * 100000),
//       date: new Date().toLocaleString(),
//       email,
//       cart,
//       subtotal,
//       discount: discountInfo.discountAmount,
//       gst,
//       platformFee,
//       surcharge,
//       convenienceFee,
//       finalAmount,
//       paymentStatus: paymentResult.status
//     };

//     if (confirm("Save invoice locally?")) {
//       localStorage.setItem("karazon_invoice", JSON.stringify(invoice));
//       console.log("Invoice saved in localStorage ✅");
//     }

//     /* ===== LAB 13: Callback to Display Invoice ===== */
//     completeBilling((inv) => {
//       console.clear();
//       console.log("========== KARAZON INVOICE ==========");
//       console.table(inv.cart);
//       console.log("Subtotal:", inv.subtotal);
//       console.log("Discount:", inv.discount);
//       console.log("GST:", inv.gst);
//       console.log("Platform Fee:", inv.platformFee);
//       console.log("Surcharge:", inv.surcharge);
//       console.log("Convenience Fee:", inv.convenienceFee);
//       console.log("FINAL AMOUNT PAYABLE:", inv.finalAmount);
//       console.log("Payment Status:", inv.paymentStatus);
//       console.log("====================================");
//       console.log("PAYMENT SUCCESSFUL ✅");
//       console.log("INVOICE GENERATED");
//     }, invoice);

//   } catch (err) {
//     if (err instanceof ValidationError) alert("Validation Error: " + err.message);
//     else alert("Unexpected Error: " + err.message);
//   } finally {
//     console.log("Thank you for shopping at Karazon.com 🎉");
//   }
// })();


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

        // console.clear();
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
