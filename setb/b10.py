from ._model import P, Q

PAPER = {
    'code': 'B10',
    'title': 'Costs, break-even, budgets & variances (Syllabus 5.4 & 5.5)',
    'theme': 'Knowledge recall: types of cost, full & contribution costing, break-even analysis, budgets and variances.',
    'time': '35 minutes',
    'questions': [
        Q([
            P('a', 'Define \u2018fixed costs\u2019.', 1, ['Costs that do not change with output, e.g. rent (1).']),
            P('b', 'Define \u2018variable costs\u2019.', 1, ['Costs that change directly with output, e.g. materials (1).']),
            P('c', 'Distinguish between direct and indirect costs.', 2, ['Direct: attributable to a specific product/cost centre (1); indirect (overheads): cannot be directly attributed (1).']),
        ]),
        Q([
            P('a', 'Define \u2018total cost\u2019.', 1, ['Fixed costs plus total variable costs (1).']),
            P('b', 'Define \u2018average (unit) cost\u2019.', 1, ['Total cost divided by output (1).']),
            P('c', 'Define \u2018marginal cost\u2019.', 2, ['The cost of producing one extra unit of output (2).']),
        ]),
        Q([
            P('a', 'State why accurate cost information is important.', 2, ['For pricing decisions (1) and to monitor/control performance and calculate profit (1).']),
            P('b', 'State one use of cost information.', 1, ['Pricing, budgeting, make-or-buy, special orders, profit calculation (1).']),
        ]),
        Q([
            P('a', 'Distinguish between full costing and contribution costing.', 2, ['Full (absorption): allocates all costs including overheads to each product (1); contribution: charges only variable costs, fixed costs treated as a period cost (1).']),
            P('b', 'State one limitation of full costing.', 1, ['Overhead allocation is often arbitrary, distorting product costs (1).']),
        ]),
        Q([
            P('a', 'Define \u2018contribution per unit\u2019.', 2, ['Selling price per unit (1) minus variable cost per unit (1).']),
            P('b', 'State the formula for total contribution.', 1, ['Contribution per unit \u00d7 quantity sold (1).']),
        ]),
        Q([
            P('a', 'Distinguish between contribution and profit.', 2, ['Contribution = sales minus variable costs (covers fixed costs first) (1); profit = total contribution minus fixed costs (1).']),
            P('b', 'State one situation where contribution costing is useful.', 2, ['Special-order/make-or-buy decisions or break-even analysis (1) where fixed costs are already covered (1).']),
        ]),
        Q([
            P('a', 'Define \u2018break-even level of output\u2019.', 2, ['The output at which total revenue equals total cost (1) \u2013 no profit or loss (1).']),
            P('b', 'State the formula for break-even output.', 2, ['Break-even = fixed costs / contribution per unit (2).']),
        ]),
        Q([
            P('a', 'Define \u2018margin of safety\u2019.', 2, ['The amount by which actual/current output exceeds the break-even output (1) \u2013 how far sales can fall before a loss (1).']),
            P('b', 'State the formula for margin of safety.', 1, ['Margin of safety = actual output \u2212 break-even output (1).']),
        ]),
        Q([
            P('', 'A firm has fixed costs of $30,000, price $20 and variable cost $8. State the contribution per unit and the break-even output.', 4, ['=Contribution = 20 \u2212 8 = $12 (2)', '=Break-even = 30,000 / 12 = 2,500 units (2)']),
        ]),
        Q([
            P('a', 'State two uses of break-even analysis.', 2, ['Any two: set output/sales targets, assess price/cost changes, support finance applications, find margin of safety (1 each).']),
            P('b', 'State two limitations of break-even analysis.', 2, ['Any two: assumes all output sold, constant price/costs, ignores discounts/economies of scale, only as good as the data (1 each).']),
        ]),
        Q([
            P('a', 'State what the break-even point is on a break-even chart.', 2, ['Where the total revenue line crosses the total cost line (1) \u2013 output where TR = TC (1).']),
            P('b', 'State what the area beyond break-even (up to current output) represents.', 1, ['Profit (and the margin of safety) (1).']),
        ]),
        Q([
            P('a', 'Explain how contribution helps a special-order decision.', 2, ['Accept if the price exceeds variable cost (positive contribution) (1), since fixed costs are already covered it adds to profit (1).']),
            P('b', 'State one situation where contribution costing should not be used for pricing.', 1, ['Long-term/all pricing \u2013 fixed costs must eventually be covered (1).']),
        ]),
        Q([
            P('a', 'Define \u2018budget\u2019.', 2, ['A financial plan for a future period (1) setting out expected income and/or expenditure (1).']),
            P('b', 'State two purposes of budgeting.', 2, ['Any two: planning, control/monitoring, motivation, coordination, resource allocation (1 each).']),
        ]),
        Q([
            P('a', 'Define \u2018incremental budget\u2019.', 2, ['A budget based on the previous period\u2019s figures (1) adjusted by a set amount/percentage (1).']),
            P('b', 'Define \u2018zero-based budget\u2019.', 2, ['A budget where every item must be justified from zero each period (1) rather than based on the past (1).']),
        ]),
        Q([
            P('a', 'Define \u2018flexible budget\u2019.', 2, ['A budget adjusted to reflect the actual level of activity/output (1) so costs are compared at the achieved output (1).']),
            P('b', 'State one advantage of zero-based budgeting.', 1, ['Avoids carrying forward waste, forces justification/efficiency (1).']),
        ]),
        Q([
            P('', 'State four uses of budgets.', 4, ['Any four: planning, allocating resources, controlling/monitoring, measuring performance, motivating staff, coordination (1 each).']),
        ]),
        Q([
            P('a', 'Define \u2018variance\u2019.', 2, ['The difference between a budgeted figure and the actual figure (1) for income or costs (1).']),
            P('b', 'Distinguish between a favourable and an adverse variance.', 2, ['Favourable: actual is better than budget (higher revenue/profit or lower cost) (1); adverse: actual is worse than budget (1).']),
        ]),
        Q([
            P('', 'Budgeted cost was $50,000; actual cost was $57,000. State the variance and its type.', 3, ['=Variance = 57,000 \u2212 50,000 = $7,000 higher cost (2)', '$7,000 ADVERSE (1)']),
        ]),
        Q([
            P('', 'Budgeted revenue was $120,000; actual revenue was $135,000. State the variance and its type.', 3, ['=Variance = 135,000 \u2212 120,000 = $15,000 higher revenue (2)', '$15,000 FAVOURABLE (1)']),
        ]),
        Q([
            P('a', 'State one benefit of investigating variances.', 1, ['Identifies problems/successes early for corrective action (1).']),
            P('b', 'State why a favourable variance is not always good.', 2, ['It may reflect cut corners/quality or under-investment (1), or an unrealistic budget (1).']),
        ]),
    ],
}
