from ._model import P, Q

PAPER = {
    'number': 16,
    'title': 'Mixed / synoptic paper (all AS topics)',
    'theme': 'Synoptic \u2013 draws on the whole AS syllabus (enterprise, structure, HRM, marketing, operations and finance), as in a real 9609 examination.',
    'time': '1 hour 45 minutes',
    'sectionA': [
        Q([
            P('a', 'Define \u2018added value\u2019.', 2, ['Difference between the price a customer pays and the cost of bought-in inputs (2).']),
            P('b', 'Explain two ways a business could increase the value it adds.', 6, [
                'Branding/USP to justify a higher price; improved design/features.',
                'Reducing input costs (bulk buying/efficiency) without cutting price.',
                '#Marks', 'Up to 3 per way.',
            ]),
        ]),
        Q([
            P('a', 'Define \u2018limited liability\u2019.', 2, ['Owners\u2019 losses are limited to the amount they invested (1); personal assets are protected (1).']),
            P('b', 'Explain one reason a growing business might change from a partnership to a private limited company.', 4, ['Limited liability, easier to raise capital, continuity. 1\u20132 + development.']),
        ]),
        Q([
            P('a', 'Define \u2018labour turnover\u2019.', 2, ['Percentage of the workforce leaving over a period (2).']),
            P('b', 'Analyse two consequences of high labour turnover.', 6, [
                'Higher recruitment/training costs; loss of experienced staff.',
                'Disruption, lower morale and poorer customer service.',
                'L|Level 2 (4-6)|Two consequences analysed.',
                'L|Level 1 (1-3)|Identifies, limited development.',
            ]),
        ]),
        Q([
            P('a', 'Distinguish between financial and non-financial motivators.', 4, [
                'Financial: money-based rewards (pay, bonus, commission) (2).',
                'Non-financial: non-monetary methods (job enrichment, recognition, empowerment) (2).',
            ]),
            P('b', 'Explain one non-financial method of motivation.', 3, ['Job enrichment/empowerment/teamwork/recognition \u2013 developed. 1 + 2.']),
        ]),
        Q([
            P('a', 'Define \u2018market segmentation\u2019.', 2, ['Dividing a market into distinct groups with similar characteristics/needs (2).']),
            P('b', 'Explain two benefits of market segmentation.', 6, [
                'More precise targeting -> less waste/higher response.',
                'Tailored products/prices -> higher satisfaction/premium.',
                '#Marks', 'Up to 3 per benefit.',
            ]),
        ]),
        Q([
            P('a', 'Define \u2018capacity utilisation\u2019.', 2, ['Percentage of maximum output currently being used (2).']),
            P('b', 'A firm produces 8,400 units against a maximum of 12,000. Calculate capacity utilisation and explain one problem of low utilisation.', 5, [
                '=(8,400 / 12,000) \u00d7 100 = 70%',
                'Low utilisation spreads fixed costs over few units -> high unit cost/low profit.',
                '2 calc + up to 3 explanation.',
            ]),
        ]),
        Q([
            P('a', 'Define \u2018contribution per unit\u2019.', 2, ['Selling price per unit minus variable cost per unit (2).']),
            P('b', 'A product sells for $30, variable cost $18, fixed costs $48,000. Calculate the break-even output.', 4, [
                '=Contribution = 30 \u2212 18 = $12',
                '=Break-even = 48,000 / 12 = 4,000 units',
                '2 + 2.',
            ]),
        ]),
        Q([
            P('a', 'Distinguish between cash and profit.', 4, [
                'Profit = revenue \u2212 expenses (accruals); cash = actual money in/out (timing differs) (2+2).',
            ]),
            P('b', 'Explain why a profitable business can run out of cash.', 3, ['Cash tied up in receivables/inventory or spent on assets/loan repayment while profit is only on paper. 1 + 2.']),
        ]),
        Q([
            P('a', 'Define \u2018corporate social responsibility (CSR)\u2019.', 2, ['A business acting ethically and considering its impact on society and the environment (2).']),
            P('b', 'Analyse one benefit and one cost of CSR to a business.', 6, [
                'Benefit: reputation/loyalty, staff motivation, differentiation.',
                'Cost: higher operating costs may reduce short-term profit.',
                'L|Level 2 (4-6)|Both sides analysed.',
                'L|Level 1 (1-3)|Identifies, limited development.',
            ]),
        ]),
        Q([
            P('a', 'Define \u2018variance\u2019.', 2, ['Difference between a budgeted figure and the actual figure (2).']),
            P('b', 'Budgeted profit was $90,000; actual was $78,000. Calculate the variance and state its type.', 3, [
                '=90,000 \u2212 78,000 = $12,000 lower profit -> $12,000 ADVERSE',
                '2 + 1.',
            ]),
        ]),
    ],
    'sectionB': [
        Q([
            P('a', 'Analyse how the objectives of a business might change as it moves from start-up to a large plc.', 8, [
                'Start-up: survival/cash flow; growth phase: market share/expansion.',
                'Established plc: profit maximisation/shareholder value, possibly CSR.',
                'Objectives shift with ownership, size, competition and the economy.',
                'L|Level 3 (6-8)|Developed analysis.', 'L|Level 2 (3-5)|Some.',
                'L|Level 1 (1-2)|Identification.',
            ]),
            P('b', 'Evaluate whether motivation or effective management is more important to business success.', 12, [
                'Motivation: raises productivity, quality, retention; but needs direction.',
                'Management: plans, organises, controls and leads; poor management wastes a motivated workforce.',
                'Judgement: interdependent \u2013 good management creates the conditions for motivation; neither sufficient alone. Depends on context.',
                'L|Level 4 (10-12)|Balanced, supported judgement.',
                'L|Level 3 (7-9)|Balanced.', 'L|Level 2 (4-6)|Limited.', 'L|Level 1 (1-3)|One-sided.',
            ]),
        ]),
        Q([
            P('a', 'Analyse how a business could use the marketing mix to launch a new product successfully.', 8, [
                'Product: clear USP meeting researched needs; Price: penetration/skimming as appropriate.',
                'Promotion: targeted (often digital) to build awareness; Place: suitable channels.',
                'The 4Ps must be consistent.',
                'L|Level 3 (6-8)|Developed, applied analysis.', 'L|Level 2 (3-5)|Some.',
                'L|Level 1 (1-2)|Identification.',
            ]),
            P('b', 'Evaluate the view that finance is the most important functional area for a new business.', 12, [
                'For: without cash/finance the business cannot start, operate or survive; cash-flow failure is a top cause of collapse.',
                'Against: marketing (demand), operations (delivery) and HRM (people) are equally vital; weak in any area causes failure; areas are interdependent.',
                'Judgement: finance is critical for survival, especially early on, but success needs all functions working together. Depends on stage/context.',
                'L|Level 4 (10-12)|Balanced, supported judgement.',
                'L|Level 3 (7-9)|Balanced.', 'L|Level 2 (4-6)|Limited.', 'L|Level 1 (1-3)|One-sided.',
            ]),
        ]),
        Q([
            P('a', 'Analyse how improving productivity could affect a business\u2019s costs and competitiveness.', 8, [
                'Higher output per worker/machine -> lower unit costs.',
                'Enables lower prices or higher margins and faster delivery.',
                'Improves competitiveness; but investment/training cost and possible job cuts.',
                'L|Level 3 (6-8)|Developed analysis.', 'L|Level 2 (3-5)|Some.',
                'L|Level 1 (1-2)|Identification.',
            ]),
            P('b', 'Evaluate whether a business should always prioritise the interests of its shareholders over other stakeholders.', 12, [
                'For: owners risk capital; profit funds survival/investment.',
                'Against: ignoring employees, customers, community harms reputation, morale and long-term value; stakeholder balance often best serves shareholders long-term.',
                'Judgement: depends on time horizon; balancing stakeholders usually maximises long-run shareholder value.',
                'L|Level 4 (10-12)|Balanced, supported judgement.',
                'L|Level 3 (7-9)|Balanced.', 'L|Level 2 (4-6)|Limited.', 'L|Level 1 (1-3)|One-sided.',
            ]),
        ]),
        Q([
            P('a', 'Analyse the factors a business should consider when choosing a source of finance for expansion.', 8, [
                'Cost (interest/fees/dividends), need to retain control, use (short vs long term).',
                'Existing gearing/level of debt, flexibility, and risk.',
                'Match the source to the purpose.',
                'L|Level 3 (6-8)|Developed analysis.', 'L|Level 2 (3-5)|Some.',
                'L|Level 1 (1-2)|Identification.',
            ]),
            P('b', '\u2018A business that manages its people well will succeed.\u2019 Evaluate this view.', 12, [
                'For: motivated, skilled, well-led staff raise productivity, quality, service and innovation.',
                'Against: also needs the right product, market, operations and finance; external factors (recession, competition) matter; good HRM is necessary but not sufficient.',
                'Judgement: people management is a major driver but success requires all functions and a viable strategy. Depends on context.',
                'L|Level 4 (10-12)|Balanced, supported judgement.',
                'L|Level 3 (7-9)|Balanced.', 'L|Level 2 (4-6)|Limited.', 'L|Level 1 (1-3)|One-sided.',
            ]),
        ]),
    ],
    'case': {
        'title': 'Zephyr Sportswear \u2013 a whole-business decision',
        'context': [
            'Zephyr Sportswear is a private limited company making premium athletic clothing. Demand is growing and Zephyr is considering a major expansion: a new automated factory, entry into a new overseas market, and a large recruitment drive. It must decide how to finance the expansion, how to market to the new country, how to organise production, and how to motivate a rapidly growing workforce.',
            'Zephyr currently sells online (direct) at premium prices, with a strong brand and loyal customers. The finance director is cautious about rising debt; the marketing director wants to protect the premium brand; the operations director worries about quality if production is scaled up too fast.',
        ],
        'exhibits': [
            {'type': 'table', 'title': 'Table 1: Zephyr summary data',
             'headers': ['Measure', 'Value'],
             'rows': [['Revenue', '$14.6m'],
                      ['Net profit margin', '11%'],
                      ['Selling price (avg garment)', '$60'],
                      ['Variable cost (avg garment)', '$27'],
                      ['Annual fixed costs', '$5.28m'],
                      ['Existing long-term debt', 'low']],
             'col_w': [3, 1], 'align': ['left', 'right']},
        ],
        'questions': [
            Q([P('', 'Define the term \u2018brand\u2019.', 2, ['A name/design/symbol that identifies a product and differentiates it from competitors (2).'])]),
            Q([P('', 'Calculate the contribution per garment.', 2, ['=Contribution = 60 \u2212 27 = $33 per garment'])]),
            Q([P('', 'Using the data, calculate Zephyr\u2019s break-even output (garments per year).', 3, [
                '=Break-even = fixed costs / contribution = 5,280,000 / 33 = 160,000 garments per year',
                '2 method + 1 answer (160,000).',
            ])]),
            Q([P('', 'Explain one reason Zephyr should protect its premium brand during expansion.', 4, [
                'The premium brand supports high price/margin (contribution $33) and loyalty; scaling up carelessly could dilute quality/image and lose the price premium.',
                '1\u20132 + development.',
            ])]),
            Q([P('', 'Analyse how Zephyr should finance the expansion, given the directors\u2019 concerns.', 8, [
                'Low existing debt and 11% margin mean a bank loan is affordable and keeps control (no dilution).',
                'Retained earnings could part-fund it, protecting cash; avoid over-gearing to satisfy the cautious finance director.',
                'Consider matching long-term finance (loan) to long-life assets (factory).',
                'L|Level 3 (6-8)|Developed analysis using data/constraints.',
                'L|Level 2 (3-5)|Some.', 'L|Level 1 (1-2)|Identification.',
            ])]),
            Q([P('', 'Recommend how Zephyr should manage the expansion across marketing, operations and finance to protect its brand and grow successfully. Justify your answer.', 12, [
                '#Marketing', 'Enter the new market with the premium positioning and USP; targeted digital promotion; keep selective (direct/online) distribution to protect the brand.',
                '#Operations', 'Scale up gradually with quality control; automation to meet demand and cut unit cost without sacrificing quality; keep some premium lines carefully managed.',
                '#Finance', 'Fund via retained earnings + a moderate loan (low gearing, keeps control), staged to manage cash.',
                '#Judgement', 'Supported, integrated recommendation that balances growth with brand protection and financial prudence; phase the expansion to control quality and risk. Use figures (margin, break-even, low debt).',
                'L|Level 4 (10-12)|Balanced, synoptic, uses data, justified recommendation.',
                'L|Level 3 (7-9)|Balanced, some judgement/application.',
                'L|Level 2 (4-6)|Limited.', 'L|Level 1 (1-3)|One-sided/assertion.',
            ])]),
        ],
    },
}
