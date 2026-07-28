from ._model import P, Q

PAPER = {
    'number': 14,
    'title': 'Cash flow, costs, contribution and break-even',
    'theme': 'Syllabus 5.3 & 5.4 \u2013 Cash flow forecasts, types of cost, full and contribution costing, using cost information, and break-even analysis.',
    'time': '1 hour 45 minutes',
    'sectionA': [
        Q([
            P('a', 'Define \u2018cash flow forecast\u2019.', 2, ['An estimate of the expected cash inflows and outflows of a business (1) over a future period, showing opening/closing balances (1).']),
            P('b', 'Explain two benefits of producing a cash flow forecast.', 6, [
                'Identifies potential cash shortages in advance so action can be taken (arrange overdraft).',
                'Supports loan applications and planning; monitors performance.',
                'Helps time spending/investment.',
                '#Marks', 'Up to 3 per benefit.',
            ]),
        ]),
        Q([
            P('a', 'A business has an opening cash balance of $12,000, receipts of $34,000 and payments of $41,000 in a month. Calculate the closing balance.', 3, [
                '=Net cash flow = 34,000 \u2212 41,000 = \u2212$7,000',
                '=Closing balance = 12,000 + (\u22127,000) = $5,000',
                '2 method + 1 answer ($5,000).',
            ]),
            P('b', 'Explain one way this business could improve its cash flow.', 3, ['Delay payments/negotiate credit, chase receivables, cut costs, arrange overdraft, delay capital spending, sale and leaseback. 1 + 2.']),
        ]),
        Q([
            P('a', 'Distinguish between fixed costs and variable costs.', 4, [
                'Fixed costs: do not change with output (e.g. rent) (2).',
                'Variable costs: change directly with output (e.g. materials) (2).',
            ]),
            P('b', 'Distinguish between direct and indirect costs.', 3, ['Direct: can be attributed to a specific product/cost centre (e.g. direct materials); indirect (overheads): cannot (e.g. admin). 1\u20132 + development.']),
        ]),
        Q([
            P('a', 'Define \u2018contribution\u2019 (per unit).', 2, ['Selling price per unit minus variable cost per unit (1); it contributes towards fixed costs and then profit (1).']),
            P('b', 'A product sells for $20 with variable cost $12. Calculate contribution per unit and total contribution from 5,000 units.', 4, [
                '=Contribution per unit = 20 \u2212 12 = $8',
                '=Total contribution = 8 \u00d7 5,000 = $40,000',
                '2 + 2.',
            ]),
        ]),
        Q([
            P('a', 'Explain the difference between contribution and profit.', 4, [
                'Contribution = sales revenue minus total variable costs (covers fixed costs first).',
                'Profit = total contribution minus fixed costs; profit only arises once fixed costs are covered.',
            ]),
            P('b', 'State one use of contribution costing.', 3, ['Break-even analysis, special-order/make-or-buy decisions, product profitability, pricing. 1 + 2.']),
        ]),
        Q([
            P('a', 'Define \u2018break-even level of output\u2019.', 2, ['The level of output at which total revenue equals total costs (1), so the business makes neither profit nor loss (1).']),
            P('b', 'A firm has fixed costs of $60,000, price $25 and variable cost $10 per unit. Calculate the break-even output.', 4, [
                '=Contribution per unit = 25 \u2212 10 = $15',
                '=Break-even = fixed costs / contribution = 60,000 / 15 = 4,000 units',
                '2 + 2.',
            ]),
        ]),
        Q([
            P('a', 'Define \u2018margin of safety\u2019.', 2, ['The amount by which current/actual output exceeds the break-even output (1); how far sales can fall before a loss (1).']),
            P('b', 'Using the previous firm (break-even 4,000 units), calculate the margin of safety and profit if it sells 7,000 units.', 4, [
                '=Margin of safety = 7,000 \u2212 4,000 = 3,000 units',
                '=Profit = margin of safety \u00d7 contribution = 3,000 \u00d7 15 = $45,000 (or total contribution 7,000\u00d715=105,000 \u2212 FC 60,000 = $45,000)',
                '2 + 2.',
            ]),
        ]),
        Q([
            P('a', 'Distinguish between full costing and contribution costing.', 4, [
                'Full (absorption) costing: allocates all costs, including a share of overheads, to each product (2).',
                'Contribution costing: charges only variable costs to products; fixed costs treated as a period cost (2).',
            ]),
            P('b', 'Explain one limitation of full costing.', 3, ['Overhead allocation is often arbitrary, which can distort product costs/decisions. 1 + 2.']),
        ]),
        Q([
            P('a', 'Explain how contribution costing can help with a special order decision.', 4, ['Accept an order if its price exceeds variable cost (positive contribution), since fixed costs are already covered \u2013 it adds to profit. 1\u20132 + development.']),
            P('b', 'State one situation where contribution costing should NOT be used for pricing.', 3, ['Long-term/all pricing (fixed costs must be covered eventually); if spare capacity is not available; risk of undercharging. 1 + 2.']),
        ]),
        Q([
            P('a', 'State two uses of break-even analysis.', 2, ['Any two: set output/sales targets, assess effect of price/cost changes, support finance applications, judge margin of safety, aid decision-making.']),
            P('b', 'Analyse two limitations of break-even analysis.', 6, [
                'Assumes all output is sold and costs/price are constant (linear) \u2013 unrealistic.',
                'Ignores discounts/economies of scale; only as good as the data; static (one snapshot).',
                'L|Level 2 (4-6)|Two limitations analysed with development.',
                'L|Level 1 (1-3)|Identifies limitations, limited development.',
            ]),
        ]),
    ],
    'sectionB': [
        Q([
            P('a', 'Analyse how a cash flow forecast can help a business avoid a liquidity crisis.', 8, [
                'Predicts months of negative closing balance in advance -> arrange finance/overdraft early.',
                'Guides timing of spending, credit terms and stock purchases.',
                'Provides an early-warning control tool; but only as accurate as its assumptions.',
                'L|Level 3 (6-8)|Developed, applied analysis.', 'L|Level 2 (3-5)|Some.',
                'L|Level 1 (1-2)|Identification.',
            ]),
            P('b', 'Evaluate the usefulness of break-even analysis to a small manufacturer.', 12, [
                'For: simple, shows break-even output, margin of safety and effect of price/cost changes; aids planning and finance applications.',
                'Against: assumes constant price/costs and that all output is sold; ignores discounts/economies of scale; data may be inaccurate; static in a changing market.',
                'Judgement: a useful quick planning/decision tool if assumptions are understood; should be combined with realistic forecasts, not relied on alone.',
                'L|Level 4 (10-12)|Balanced, supported judgement.',
                'L|Level 3 (7-9)|Balanced.', 'L|Level 2 (4-6)|Limited.', 'L|Level 1 (1-3)|One-sided.',
            ]),
        ]),
        Q([
            P('a', 'Analyse how accurate cost information helps a business make better decisions.', 8, [
                'Informs pricing (cover costs + margin), product mix and make-or-buy/special orders.',
                'Enables cost control, budgeting and profit calculation.',
                'Poor cost data -> mispricing/loss-making decisions.',
                'L|Level 3 (6-8)|Developed analysis.', 'L|Level 2 (3-5)|Some.',
                'L|Level 1 (1-2)|Identification.',
            ]),
            P('b', 'Evaluate whether contribution costing is more useful than full costing for decision-making.', 12, [
                'For contribution: avoids arbitrary overhead allocation, ideal for short-term/special-order/make-or-buy and break-even decisions.',
                'Against: ignores fixed costs which must be covered long-term; risk of under-pricing; full costing better for long-run pricing and product profitability.',
                'Judgement: contribution is better for short-term marginal decisions with spare capacity; full costing for long-term pricing. Depends on the decision. Use both.',
                'L|Level 4 (10-12)|Balanced, supported judgement.',
                'L|Level 3 (7-9)|Balanced.', 'L|Level 2 (4-6)|Limited.', 'L|Level 1 (1-3)|One-sided.',
            ]),
        ]),
        Q([
            P('a', 'Analyse how a business could use break-even analysis to assess the effect of raising its selling price.', 8, [
                'Higher price raises contribution per unit -> lowers break-even output and raises margin of safety/profit at a given volume.',
                'But higher price may reduce quantity demanded (not shown on chart) \u2013 sales could fall.',
                'Chart shifts: total revenue line steeper, break-even point left.',
                'L|Level 3 (6-8)|Developed analysis with the model.',
                'L|Level 2 (3-5)|Some.', 'L|Level 1 (1-2)|Identification.',
            ]),
            P('b', '\u2018Cash flow is more important than profit for a new business.\u2019 Evaluate this view.', 12, [
                'For: new firms fail from running out of cash even if profitable on paper; cash pays wages/suppliers and ensures survival.',
                'Against: without profit long-term the business is not viable; profit funds growth and attracts investors; both matter.',
                'Judgement: in the short term/start-up phase cash is critical for survival; profit is essential for long-term viability \u2013 both needed, cash more urgent early on.',
                'L|Level 4 (10-12)|Balanced, supported judgement.',
                'L|Level 3 (7-9)|Balanced.', 'L|Level 2 (4-6)|Limited.', 'L|Level 1 (1-3)|One-sided.',
            ]),
        ]),
        Q([
            P('a', 'Analyse the assumptions on which break-even analysis is based.', 8, [
                'Selling price constant at all output levels; variable cost per unit constant; fixed costs constant.',
                'All output produced is sold (no inventory build-up); single product/mix.',
                'These simplify reality and limit accuracy.',
                'L|Level 3 (6-8)|Developed analysis of assumptions.',
                'L|Level 2 (3-5)|Some.', 'L|Level 1 (1-2)|Lists assumptions.',
            ]),
            P('b', 'Evaluate how useful a cash flow forecast is, given that it is based on estimates.', 12, [
                'For: even estimates reveal likely shortfalls, aid planning and finance; can be updated (rolling forecast); better than no plan.',
                'Against: inaccurate assumptions (sales, timing, costs) can mislead; unexpected events not captured; false confidence.',
                'Judgement: useful as a flexible planning/monitoring tool if regularly revised and realistic; not a guarantee. Depends on quality of assumptions.',
                'L|Level 4 (10-12)|Balanced, supported judgement.',
                'L|Level 3 (7-9)|Balanced.', 'L|Level 2 (4-6)|Limited.', 'L|Level 1 (1-3)|One-sided.',
            ]),
        ]),
    ],
    'case': {
        'title': 'Break-even and cash at Piatto Pizza',
        'context': [
            'Piatto Pizza is opening a new outlet. Each pizza sells for $9.00, with variable costs (ingredients, packaging, direct labour) of $3.60. Monthly fixed costs (rent, salaries, utilities) are $16,200. The owner has prepared a partial cash flow forecast and wants to know the break-even level of sales and the margin of safety at the expected volume of 4,000 pizzas per month.',
            'The owner is also considering a one-off catering order of 500 pizzas at a special price of $5.00 each, which some staff think should be rejected because it is \u2018below the normal price\u2019. There is spare capacity to fulfil it.',
        ],
        'exhibits': [
            {'type': 'diagram', 'name': 'breakeven', 'caption': 'Fig 1: Break-even chart (illustrative). Use the figures to calculate exact values.'},
            {'type': 'table', 'title': 'Table 1: Partial monthly cash flow forecast ($)',
             'headers': ['Item', 'Month 1', 'Month 2', 'Month 3'],
             'rows': [['Opening balance', '10,000', '?', '?'],
                      ['Cash receipts', '28,000', '34,000', '39,000'],
                      ['Cash payments', '37,000', '33,000', '35,000'],
                      ['Net cash flow', '?', '?', '?'],
                      ['Closing balance', '?', '?', '?']],
             'col_w': [1.8, 1, 1, 1], 'align': ['left', 'right', 'right', 'right']},
        ],
        'questions': [
            Q([P('', 'Calculate the contribution per pizza.', 2, ['=Contribution = 9.00 \u2212 3.60 = $5.40 per pizza'])]),
            Q([P('', 'Calculate the break-even level of output per month (in pizzas).', 3, [
                '=Break-even = fixed costs / contribution = 16,200 / 5.40 = 3,000 pizzas per month',
                '2 method + 1 answer (3,000).',
                'DIAG|breakeven|Worked chart: TR = $9.00Q, TC = $16,200 + $3.60Q. Break-even where they cross at 3,000 pizzas (revenue = $27,000). At 4,000 pizzas the margin of safety is 1,000 pizzas and profit is $5,400.',
            ])]),
            Q([P('', 'Calculate the margin of safety and monthly profit at the expected volume of 4,000 pizzas.', 4, [
                '=Margin of safety = 4,000 \u2212 3,000 = 1,000 pizzas',
                '=Profit = (4,000 \u00d7 5.40) \u2212 16,200 = 21,600 \u2212 16,200 = $5,400 per month',
                '2 + 2.',
            ])]),
            Q([P('', 'Complete the cash flow forecast (Table 1): calculate the net cash flow and closing balance for each month.', 6, [
                '=Month 1: net = 28,000 \u2212 37,000 = \u2212$9,000; closing = 10,000 \u2212 9,000 = $1,000',
                '=Month 2: net = 34,000 \u2212 33,000 = +$1,000; opening 1,000 -> closing = $2,000',
                '=Month 3: net = 39,000 \u2212 35,000 = +$4,000; opening 2,000 -> closing = $6,000',
                '2 marks per month (net + closing), max 6. Own-figure rule applies.',
            ])]),
            Q([P('', 'Advise whether Piatto should accept the special catering order of 500 pizzas at $5.00 each.', 5, [
                '=Special-order contribution = (5.00 \u2212 3.60) \u00d7 500 = 1.40 \u00d7 500 = $700 extra contribution.',
                'With spare capacity and fixed costs already covered, the order adds $700 profit -> accept on contribution grounds.',
                'Caution: do not let regular customers expect the $5 price (may undermine normal pricing); ensure it does not displace full-price sales.',
                'L|Level 2 (3-5)|Correct contribution calc + reasoned advice with a caveat.',
                'L|Level 1 (1-2)|Some calculation/assertion.',
            ])]),
            Q([P('', 'Evaluate whether break-even analysis alone is a reliable basis for the owner\u2019s decisions.', 12, [
                '#Strengths', 'Quick, shows break-even (3,000), margin of safety (1,000) and profit ($5,400); useful for planning and pricing.',
                '#Weaknesses', 'Assumes constant $9 price and $3.60 variable cost and that all pizzas are sold; ignores demand changes, wastage, seasonality; the special order shows real pricing is more nuanced; cash timing (Table 1 shows a $1,000 low balance in Month 1) is a separate risk.',
                '#Judgement', 'Supported judgement: break-even is a helpful guide but not sufficient alone; the owner should also use the cash flow forecast and realistic demand estimates. Not fully reliable in isolation.',
                'L|Level 4 (10-12)|Balanced, uses figures, clear judgement.',
                'L|Level 3 (7-9)|Balanced, some judgement/application.',
                'L|Level 2 (4-6)|Limited.', 'L|Level 1 (1-3)|One-sided/assertion.',
            ])]),
        ],
    },
}
