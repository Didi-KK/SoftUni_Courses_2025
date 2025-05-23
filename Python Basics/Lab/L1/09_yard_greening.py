total_sq_m_for_landscaping = float(input())
price_per_sq_m_incl_vat_lv = 7.61
total_price_for_landscaping_lv = total_sq_m_for_landscaping * price_per_sq_m_incl_vat_lv
discount_for_landscaping = 0.18
total_discount_lv = total_price_for_landscaping_lv * discount_for_landscaping
final_price_payable_lv = total_price_for_landscaping_lv - total_discount_lv

print(f"The final price is: {final_price_payable_lv} lv.")
print(f"The discount is: {total_discount_lv} lv.")

