"""Reproduce the TBA Group cement transportation linear program.
Run: python transportation_model.py
Requires: scipy>=1.9
"""
import csv
from pathlib import Path
from scipy.optimize import linprog

ROOT = Path(__file__).resolve().parent
DEPOTS = ['A', 'B', 'C', 'D']
DESTINATIONS = ['Ikeja', 'Ajagunle', 'Apapa', 'Idi-Araba', 'Agege']
SUPPLY = [1100, 1220, 950, 1830]
DEMAND = [1010, 970, 980, 1250, 890]
COST = [[68, 36, 26, 31, 62],
        [35, 72, 36, 28, 54],
        [40, 55, 41, 30, 28],
        [25, 35, 40, 80, 34]]
VAM_START = [[0, 120, 980, 0, 0],
             [0, 0, 0, 1220, 0],
             [0, 30, 0, 30, 890],
             [1010, 820, 0, 0, 0]]
PAPER_OPTIMAL = [[0, 120, 980, 0, 0],
                 [30, 0, 0, 1190, 0],
                 [0, 0, 0, 60, 890],
                 [980, 850, 0, 0, 0]]

def total_cost(allocation):
    return sum(COST[i][j] * allocation[i][j] for i in range(4) for j in range(5))

def verify(allocation):
    assert all(abs(sum(allocation[i]) - SUPPLY[i]) < 1e-6 for i in range(4)), 'Supply mismatch'
    assert all(abs(sum(allocation[i][j] for i in range(4)) - DEMAND[j]) < 1e-6 for j in range(5)), 'Demand mismatch'
    assert all(v >= -1e-6 for row in allocation for v in row), 'Negative shipment'


def solve():
    assert sum(SUPPLY) == sum(DEMAND)
    # Equality constraints: four supply rows + five demand columns.
    a_eq, b_eq = [], []
    for i in range(4):
        a_eq.append([1 if k // 5 == i else 0 for k in range(20)])
        b_eq.append(SUPPLY[i])
    for j in range(5):
        a_eq.append([1 if k % 5 == j else 0 for k in range(20)])
        b_eq.append(DEMAND[j])
    result = linprog([v for row in COST for v in row], A_eq=a_eq, b_eq=b_eq,
                     bounds=(0, None), method='highs')
    if not result.success:
        raise RuntimeError(result.message)
    solution = [[round(result.x[5*i+j], 8) for j in range(5)] for i in range(4)]
    verify(solution)
    verify(VAM_START)
    verify(PAPER_OPTIMAL)
    assert total_cost(VAM_START) == 145380
    assert total_cost(PAPER_OPTIMAL) == 145140
    assert abs(result.fun - 145140) < 1e-5
    print('VAM initial cost (NGN):', total_cost(VAM_START))
    print('Solver minimum cost (NGN):', round(result.fun, 2))
    print('Improvement (NGN):', total_cost(VAM_START) - result.fun)
    print('Solver allocation (may differ from paper if multiple optima exist):')
    for name, row in zip(DEPOTS, solution):
        print(name, [round(v, 2) for v in row])
    print('Paper allocation cost (NGN):', total_cost(PAPER_OPTIMAL))
    print('All feasibility and cost checks passed.')
    return solution

if __name__ == '__main__':
    solve()
