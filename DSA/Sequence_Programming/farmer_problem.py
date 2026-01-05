
"""
import math
from typing import Tuple


def read_float(prompt: str, default: float = None, non_negative: bool = True) -> float:
    while True:
        inp = input(f"{prompt}" + (f" [default: {default}]" if default is not None else "") + ": ").strip()
        if inp == "" and default is not None:
            val = float(default)
        else:
            try:
                val = float(inp)
            except ValueError:
                print("  ❌ Enter a valid number.")
                continue
        if math.isnan(val) or math.isinf(val):
            print("  ❌ Number must be finite.")
            continue
        if non_negative and val < 0:
            print("  ❌ Value cannot be negative.")
            continue
        return val


def read_int(prompt: str, default: int = None, min_val: int = None) -> int:
    while True:
        inp = input(f"{prompt}" + (f" [default: {default}]" if default is not None else "") + ": ").strip()
        if inp == "" and default is not None:
            val = int(default)
        else:
            try:
                val = int(inp)
            except ValueError:
                print("  ❌ Enter a valid integer.")
                continue
        if min_val is not None and val < min_val:
            print(f"  ❌ Enter an integer >= {min_val}.")
            continue
        return val


def read_percentage_pair(prompt_a: str, prompt_b: str, default_a: float, default_b: float) -> Tuple[float, float]:
    while True:
        a = read_float(prompt_a + " % (0-100)", default_a)
        b = read_float(prompt_b + " % (0-100)", default_b)
        total = a + b
        if abs(total - 100.0) > 1e-6:
            print("  ❌ Percentages must add up to 100. Please re-enter.")
            continue
        return a / 100.0, b / 100.0


def rs_per_tonne_from_kg(kg_price: float) -> float:
    return kg_price * 1000.0


def format_rs(x: float) -> str:
    return f"Rs {x:,.2f}"


def safe_multiply(a: float, b: float) -> float:
    result = a * b
    if math.isinf(result):
        raise OverflowError("Numeric overflow during multiplication")
    return result


def compute_crop_tonnes_and_revenue(
    acres: float,
    crop_name: str,
    *,
    yield_t_per_acre: float = None,
    yield_split: Tuple[Tuple[float, float], ...] = None,
    price_per_kg: float = None,
    price_per_tonne: float = None
):
    if yield_split is not None:
        total_tonnes = 0.0
        for frac, tpa in yield_split:
            acres_part = acres * frac
            total_tonnes += safe_multiply(acres_part, tpa)
    else:
        total_tonnes = safe_multiply(acres, yield_t_per_acre)

    if price_per_tonne is None:
        price_per_tonne = rs_per_tonne_from_kg(price_per_kg)

    revenue = safe_multiply(total_tonnes, price_per_tonne)
    return total_tonnes, price_per_tonne, revenue


def main():
    print("\n=== Interactive Farm Revenue Calculator ===\n")
    # Basic farm settings
    total_acres = read_float("Enter total acres of the farm", 80.0)
    segments = read_int("Enter number of equal segments (crops)", 5, min_val=1)
    acres_per_segment = total_acres / segments
    print(f"Each segment (crop) area = {acres_per_segment:.4f} acres\n")

    # Default yields & prices (per problem). User can change.
    print("Enter yields and prices for each crop. Press Enter to accept defaults shown in brackets.\n")

    # Tomato: split (30% @ 10 t/acre, 70% @ 12 t/acre) & price Rs 7/kg
    t_frac_a, t_frac_b = read_percentage_pair(
        "Tomato split fraction A (e.g. part with lower yield) - percent",
        "Tomato split fraction B (remaining) - percent",
        default_a=30.0,
        default_b=70.0,
    )
    t_yield_a = read_float("Tomato yield for fraction A (t/acre)", 10.0)
    t_yield_b = read_float("Tomato yield for fraction B (t/acre)", 12.0)
    tomato_price_per_kg = read_float("Tomato price per kg (Rs)", 7.0)

    # Potato
    potato_yield = read_float("Potato yield (t/acre)", 10.0)
    potato_price_per_kg = read_float("Potato price per kg (Rs)", 20.0)

    # Cabbage
    cabbage_yield = read_float("Cabbage yield (t/acre)", 14.0)
    cabbage_price_per_kg = read_float("Cabbage price per kg (Rs)", 24.0)

    # Sunflower
    sunflower_yield = read_float("Sunflower yield (t/acre)", 0.7)
    sunflower_price_per_kg = read_float("Sunflower price per kg (Rs)", 200.0)

    # Sugarcane
    sugarcane_yield = read_float("Sugarcane yield (t/acre)", 45.0)
    # Given price for sugarcane is per tonne already
    sugarcane_price_per_tonne = read_float("Sugarcane price per tonne (Rs)", 4000.0)

    # Conversion timeline (months when crop becomes chemical-free)
    print("\nEnter the month number when each crop becomes chemical-free (integer months).")
    veg_conv_month = read_int("Vegetables (tomato, potato, cabbage) fully chemical-free after month", 6, min_val=0)
    sunflower_conv_month = read_int("Sunflower fully chemical-free after month", 10, min_val=0)
    sugarcane_conv_month = read_int("Sugarcane fully chemical-free after month", 14, min_val=0)

    # Target month to compute 'chemical-free by this time' (user wanted 11 originally)
    target_month = read_int("\nCompute chemical-free sales by end of month (target month)", 11, min_val=0)

    # Acre allocation per crop (equal segments)
    acres_each = acres_per_segment  # same for all crops since equal division

    # Compute for each crop
    results = {}

    # Tomato
    t_yield_split = ((t_frac_a, t_yield_a), (t_frac_b, t_yield_b))
    t_tonnes, t_price_t, t_revenue = compute_crop_tonnes_and_revenue(
        acres_each, "tomato",
        yield_split=t_yield_split,
        price_per_kg=tomato_price_per_kg
    )
    results["tomato"] = {
        "acres": acres_each,
        "total_tonnes": t_tonnes,
        "price_per_tonne": t_price_t,
        "revenue": t_revenue,
        "chemical_free_month": veg_conv_month
    }

    # Potato
    p_tonnes, p_price_t, p_revenue = compute_crop_tonnes_and_revenue(
        acres_each, "potato",
        yield_t_per_acre=potato_yield,
        price_per_kg=potato_price_per_kg
    )
    results["potato"] = {
        "acres": acres_each,
        "total_tonnes": p_tonnes,
        "price_per_tonne": p_price_t,
        "revenue": p_revenue,
        "chemical_free_month": veg_conv_month
    }

    # Cabbage
    c_tonnes, c_price_t, c_revenue = compute_crop_tonnes_and_revenue(
        acres_each, "cabbage",
        yield_t_per_acre=cabbage_yield,
        price_per_kg=cabbage_price_per_kg
    )
    results["cabbage"] = {
        "acres": acres_each,
        "total_tonnes": c_tonnes,
        "price_per_tonne": c_price_t,
        "revenue": c_revenue,
        "chemical_free_month": veg_conv_month
    }

    # Sunflower
    s_tonnes, s_price_t, s_revenue = compute_crop_tonnes_and_revenue(
        acres_each, "sunflower",
        yield_t_per_acre=sunflower_yield,
        price_per_kg=sunflower_price_per_kg
    )
    results["sunflower"] = {
        "acres": acres_each,
        "total_tonnes": s_tonnes,
        "price_per_tonne": s_price_t,
        "revenue": s_revenue,
        "chemical_free_month": sunflower_conv_month
    }

    # Sugarcane
    sc_tonnes, sc_price_t, sc_revenue = compute_crop_tonnes_and_revenue(
        acres_each, "sugarcane",
        yield_t_per_acre=sugarcane_yield,
        price_per_tonne=sugarcane_price_per_tonne
    )
    results["sugarcane"] = {
        "acres": acres_each,
        "total_tonnes": sc_tonnes,
        "price_per_tonne": sc_price_t,
        "revenue": sc_revenue,
        "chemical_free_month": sugarcane_conv_month
    }

    # Summaries
    overall_sales = sum(results[c]["revenue"] for c in results)
    cf_sales = sum(results[c]["revenue"] for c in results if results[c]["chemical_free_month"] <= target_month)

    # Print table
    print("\n\n=== Revenue Breakdown ===")
    hdr = f"{'Crop':<10}{'Acres':>8}{'Tonnes':>12}{'Price/t (Rs)':>18}{'Revenue':>18}{'CF Month':>10}"
    print(hdr)
    print("-" * len(hdr))
    for crop, info in results.items():
        print(
            f"{crop:<10}"
            f"{info['acres']:8.1f}"
            f"{info['total_tonnes']:12,.1f}"
            f"{format_rs(info['price_per_tonne']):>18}"
            f"{format_rs(info['revenue']):>18}"
            f"{info['chemical_free_month']:>10d}"
        )

    print("\nSummary:")
    print(f" Overall sales from all {total_acres:.0f} acres: {format_rs(overall_sales)}")
    print(f" Sales realised from chemical-free farming by end of month {target_month}: {format_rs(cf_sales)}")

    avg_rev_per_acre = overall_sales / total_acres if total_acres else 0.0
    print(f" Average revenue per acre (overall): {format_rs(avg_rev_per_acre)}")
    print("\n(You can re-run and change any defaults to see different outcomes.)\n")


if __name__ == "__main__":
    main()"""








from typing import Dict, Any


def rs_per_tonne_from_kg_price(kg_price: float) -> float:
    """Convert Rs per kg to Rs per tonne."""
    return kg_price * 1000.0


def fmt_rs(x: float) -> str:
    """Format rupee amounts with commas and two decimals."""
    return f"Rs {x:,.2f}"


def compute_crop_revenue(acres: float, total_tonnes: float, price_per_tonne: float) -> Dict[str, float]:
    """Return revenue info for a crop."""
    revenue = total_tonnes * price_per_tonne
    revenue_per_acre = revenue / acres if acres else 0.0
    return {"acres": acres, "total_tonnes": total_tonnes,
            "price_per_tonne": price_per_tonne,
            "revenue": revenue, "revenue_per_acre": revenue_per_acre}


def main():
    # Scenario constants
    total_acres = 80.0
    segments = 5
    acres_per_segment = total_acres / segments  # 16 acres each

    # Crop definitions: yields in tonnes per acre, prices either per kg (converted) or per tonne
    crops_def: Dict[str, Dict[str, Any]] = {
        "tomato": {
            "acres": acres_per_segment,
            # special split: list of (fraction_of_tomato_land, tonnes_per_acre)
            "yield_split": [(0.30, 10.0), (0.70, 12.0)],
            "price_per_kg": 7.0
        },
        "potato": {
            "acres": acres_per_segment,
            "yield_t_per_acre": 10.0,
            "price_per_kg": 20.0
        },
        "cabbage": {
            "acres": acres_per_segment,
            "yield_t_per_acre": 14.0,
            "price_per_kg": 24.0
        },
        "sunflower": {
            "acres": acres_per_segment,
            "yield_t_per_acre": 0.7,
            "price_per_kg": 200.0
        },
        "sugarcane": {
            "acres": acres_per_segment,
            "yield_t_per_acre": 45.0,
            # price already supplied per tonne for sugarcane
            "price_per_tonne": 4000.0
        }
    }

    # Compute per-crop totals
    results = {}
    for crop, info in crops_def.items():
        acres = float(info["acres"])
        if crop == "tomato":
            # compute total tonnes using the split
            total_tonnes = 0.0
            for frac, tpa in info["yield_split"]:
                acres_part = acres * frac
                total_tonnes += acres_part * tpa
            price_per_tonne = rs_per_tonne_from_kg_price(info["price_per_kg"])
        elif crop == "sugarcane":
            total_tonnes = acres * info["yield_t_per_acre"]
            price_per_tonne = info["price_per_tonne"]
        else:
            total_tonnes = acres * info["yield_t_per_acre"]
            price_per_tonne = rs_per_tonne_from_kg_price(info["price_per_kg"])

        results[crop] = compute_crop_revenue(acres, total_tonnes, price_per_tonne)

    # Summaries
    overall_sales = sum(results[c]["revenue"] for c in results)
    # Chemical-free crops at end of 11 months: tomato, potato, cabbage, sunflower
    chemical_free_crops = ["tomato", "potato", "cabbage", "sunflower"]
    cf_sales = sum(results[c]["revenue"] for c in chemical_free_crops)

    # Print detailed breakdown
    print("\nMahesh's Farm Revenue Breakdown (per the problem scenario):")
    print("----------------------------------------------------------")
    header = f"{'Crop':<10} {'Acres':>6} {'Tonnes':>12} {'Price/t (Rs)':>15} {'Revenue':>18} {'Revenue/acre':>15}"
    print(header)
    print("-" * len(header))
    for crop, info in results.items():
        print(f"{crop:<10} {info['acres']:6.1f} {info['total_tonnes']:12,.1f} "
              f"{fmt_rs(info['price_per_tonne']):>15} {fmt_rs(info['revenue']):>18} {fmt_rs(info['revenue_per_acre']):>15}")

    print("\nSummary:")
    print("--------")
    print("Overall sales from all 80 acres: ", fmt_rs(overall_sales))
    print("Sales realisation from chemical-free farming at end of 11 months: ", fmt_rs(cf_sales))
    print()

    # Optional: also show per-acre revenue across the whole farm (average)
    avg_revenue_per_acre = overall_sales / total_acres
    print("Average revenue per acre (overall):", fmt_rs(avg_revenue_per_acre))
    print()


if __name__ == "__main__":
    main()
