# TBA Group Video Presentation — Speaker Guide
Target: approximately 9–10 minutes, including transitions.

## Jason — Introduction (about 1:45)
Good day, everyone. We are the TBA Group, presenting Optimization of Cement Distribution from Depots Using a Transportation Model. The study concerns MAISANGO Cement Nigeria Plc and the problem of shipping cement economically from four depots to five destinations. Our goal is to minimize transportation costs while using all available supply and satisfying demand. We replicate the reported case, evaluate the VAM starting solution, and verify the final cost mathematically and computationally.

## Eloisa — Preliminaries and model (about 1:40)
The transportation model is a linear programming model. Four depots supply 5,100 bags, and five destinations demand exactly 5,100 bags, making this a balanced problem. Let x sub i j represent bags sent from depot i to destination j. We minimize the sum of shipping cost per bag times bags shipped, subject to depot supply equalities, destination demand equalities, and nonnegative shipments. The model has 20 decision variables.

## Patricia — Methods and implementation (about 1:55)
The case compares Northwest Corner, Vogel's Approximation, Least Cost, and Row Minima starting methods. We reproduced the reported VAM starting allocation costing 145,380 Nigerian Naira. We then used the Modified Distribution Method, or MODI, to assess whether the starting plan could improve. A negative reduced cost of eight Nigerian Naira per bag on an unused route supported a 30-bag adjustment, reducing cost by 240 Naira. We also verified the result using WPS Solver with Simplex LP and a Python linear programming implementation. [Show terminal running python transportation_model.py.]

## Jamir — Results and discussion (about 1:55)
The optimal plan ships A to Ajagunle 120 and Apapa 980; B to Ikeja 30 and Idi-Araba 1,190; C to Idi-Araba 60 and Agege 890; and D to Ikeja 980 and Ajagunle 850. All other allocations are zero. Every depot's supply and every destination's demand are met. The minimum cost is 145,140 Nigerian Naira, matching the reported case study and the WPS Solver result. This is 240 Naira less than the initial VAM cost.

## Hannah — Limitations, recommendations, conclusion (about 1:45)
The model assumes fixed shipping costs, full supply availability, and exact demand satisfaction. It omits congestion, fuel consumption, vehicle capacities, and delivery timing. Future models could include these constraints and test changing costs and demand. In conclusion, the replication confirms the reported minimum cost of 145,140 Nigerian Naira and demonstrates how operations research supports efficient distribution decisions. Thank you.

## Suggested visuals
1. Title and case context; 2. cost and supply/demand table; 3. objective and constraints; 4. VAM/MODI explanation; 5. WPS and Python demo; 6. final shipment matrix; 7. initial vs final costs; 8. limitations and conclusion; 9. references.

This guide is a condensed recording reference; use the full script provided in the chat for fuller narration.
