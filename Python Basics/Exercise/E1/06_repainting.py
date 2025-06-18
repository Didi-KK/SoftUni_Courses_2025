price_per_sq_m_plastic_cover = 1.50
price_per_liter_paint = 14.50
price_per_liter_paint_thinner = 5.00
price_for_plastic_bags = 0.40

sq_m_plastic_cover_needed = int(input())
liters_paint_needed = int(input())
liters_paint_thinner_needed = int(input())
hours_to_complete_the_job = int(input())

total_plastic_cover = price_per_sq_m_plastic_cover * (sq_m_plastic_cover_needed + 2)
total_paint = price_per_liter_paint * (liters_paint_needed + 0.10 * liters_paint_needed)
total_paint_thinner = price_per_liter_paint_thinner * liters_paint_thinner_needed
total_materials = total_plastic_cover + total_paint + total_paint_thinner + price_for_plastic_bags
workers_remuneration_per_hour = total_materials * 0.30 * hours_to_complete_the_job
total_expenses = total_materials + workers_remuneration_per_hour

print(total_expenses)
