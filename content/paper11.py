from ._model import P, Q

PAPER = {
    'number': 11,
    'title': 'Inventory management, JIT and the supply chain',
    'theme': 'Syllabus 4.2 \u2013 Purpose and costs of inventory, buffer stock, re-order level, lead time, inventory control charts, supply chain management, and JIT vs JIC.',
    'time': '1 hour 45 minutes',
    'sectionA': [
        Q([
            P('a', 'State the three types of inventory a manufacturer holds.', 3, ['Raw materials (1), work in progress (1) and finished goods (1).']),
            P('b', 'Explain two benefits to a business of holding inventory.', 6, [
                'Meets unexpected demand/avoids stock-outs and lost sales.',
                'Allows production to continue if deliveries are late (buffer).',
                'Enables bulk-buying discounts; smooths seasonal demand.',
                '#Marks', 'Up to 3 per benefit.',
            ]),
        ]),
        Q([
            P('a', 'Define \u2018buffer inventory\u2019.', 2, ['A minimum level of inventory held as a safety margin (1) to cover unexpected demand or delivery delays (1).']),
            P('b', 'Explain one cost of holding too much inventory.', 4, ['Storage, insurance, obsolescence/spoilage, and cash tied up (opportunity cost) that could be used elsewhere. 1\u20132 + development.']),
        ]),
        Q([
            P('a', 'Define \u2018lead time\u2019.', 2, ['The time between placing an order with a supplier and receiving the goods (2).']),
            P('b', 'Explain how a longer lead time affects the re-order level.', 4, ['Longer lead time means stock must be re-ordered earlier/at a higher level to avoid running out before delivery. 1\u20132 + development.']),
        ]),
        Q([
            P('a', 'Define \u2018re-order level\u2019.', 2, ['The inventory level at which a new order is automatically placed (1) to replenish stock before it runs out (1).']),
            P('b', 'On an inventory control chart, explain what the gap between maximum inventory and buffer inventory represents.', 4, ['The usable/working stock that is drawn down between deliveries; the re-order quantity brings it back to maximum. 1\u20132 + development.']),
        ], diagram={'type': 'inventory', 'caption': 'Fig: A typical inventory control chart'}),
        Q([
            P('a', 'Define \u2018Just in Time (JIT)\u2019.', 3, ['An inventory approach where materials arrive exactly when needed for production (1), minimising stock held (1) to cut holding costs (1).']),
            P('b', 'Explain one requirement for JIT to work successfully.', 3, ['Reliable suppliers/frequent deliveries, good relationships, accurate demand forecasting, quality inputs. 1 + 2.']),
        ]),
        Q([
            P('a', 'Distinguish between JIT and JIC (Just in Case).', 4, [
                'JIT: minimal stock, delivered as needed \u2013 low holding cost but vulnerable to disruption (2).',
                'JIC: holds buffer stock \u2018just in case\u2019 \u2013 secure supply but higher holding costs (2).',
            ]),
            P('b', 'Explain one situation where JIC is more appropriate than JIT.', 3, ['Unreliable supply chains, volatile demand, or where stock-outs are very costly (e.g. hospitals). 1 + 2.']),
        ]),
        Q([
            P('a', 'Define \u2018supply chain management\u2019.', 3, ['The management of the flow of materials, goods and information (1) from suppliers through production to the final customer (1) to improve efficiency and reliability (1).']),
            P('b', 'Analyse why effective supply chain management is important to a business.', 6, [
                'Ensures reliable, cost-effective supply of the right materials at the right time.',
                'Reduces costs, lead times and stock-outs; improves quality and customer satisfaction.',
                'Builds resilience against disruption.',
                'L|Level 2 (4-6)|Developed analysis of importance.',
                'L|Level 1 (1-3)|States importance, limited development.',
            ]),
        ]),
        Q([
            P('a', 'Explain what happens to inventory levels if usage suddenly rises but the re-order level is unchanged.', 4, ['Stock is drawn down faster and may fall below buffer/run out before the next delivery -> stock-out risk. 1\u20132 + development.']),
            P('b', 'State two costs of running out of inventory (a stock-out).', 3, ['Any: lost sales/revenue, dissatisfied customers, halted production, idle labour, damaged reputation. 1\u20132 + 1.']),
        ]),
        Q([
            P('a', 'Define \u2018work in progress\u2019.', 2, ['Partly finished goods that are still being processed (1) \u2013 between raw materials and finished output (1).']),
            P('b', 'Explain one way a business could reduce the amount of cash tied up in inventory.', 4, ['Adopt JIT/lower buffer, improve forecasting, faster stock turnover, better supplier links. 1\u20132 + development.']),
        ]),
        Q([
            P('a', 'Define \u2018economic order quantity\u2019 (in simple terms).', 2, ['The order size that minimises total inventory costs (1) \u2013 balancing ordering costs against holding costs (1).']),
            P('b', 'Analyse the trade-off between ordering in large batches and ordering little and often.', 6, [
                'Large batches: bulk discounts, fewer orders, but high holding cost and cash tied up/obsolescence risk.',
                'Small frequent orders (JIT): low holding cost but higher ordering/delivery cost and stock-out risk.',
                'L|Level 2 (4-6)|Developed analysis of the trade-off.',
                'L|Level 1 (1-3)|States trade-off, limited development.',
            ]),
        ]),
    ],
    'sectionB': [
        Q([
            P('a', 'Analyse the costs and benefits to a business of holding high levels of inventory.', 8, [
                'Benefits: avoids stock-outs/lost sales, buffers against delivery/demand fluctuations, bulk discounts, smooth production.',
                'Costs: storage, insurance, obsolescence, and cash tied up (opportunity cost).',
                'L|Level 3 (6-8)|Developed analysis both sides.', 'L|Level 2 (3-5)|Some.',
                'L|Level 1 (1-2)|Identification.',
            ]),
            P('b', 'Evaluate whether a manufacturer should adopt a JIT approach to inventory.', 12, [
                'For: cuts holding costs, frees cash/space, reduces waste/obsolescence, encourages efficiency and quality.',
                'Against: highly vulnerable to supply disruption (strikes, transport, global shocks), needs reliable suppliers and forecasting, loses bulk discounts, stock-out risk.',
                'Judgement: suits stable demand and reliable supply chains; risky where supply is uncertain \u2013 many now hold some buffer (hybrid). Depends on context.',
                'L|Level 4 (10-12)|Balanced, supported judgement.',
                'L|Level 3 (7-9)|Balanced.', 'L|Level 2 (4-6)|Limited.', 'L|Level 1 (1-3)|One-sided.',
            ]),
        ]),
        Q([
            P('a', 'Analyse how effective supply chain management can improve a business\u2019s competitiveness.', 8, [
                'Lower input costs and lead times -> lower prices/faster delivery.',
                'Reliable quality and availability -> customer satisfaction/retention.',
                'Resilience and flexibility to respond to demand changes.',
                'L|Level 3 (6-8)|Developed analysis.', 'L|Level 2 (3-5)|Some.',
                'L|Level 1 (1-2)|Identification.',
            ]),
            P('b', 'Evaluate the view that holding buffer inventory is a waste of money.', 12, [
                'For: buffer stock ties up cash, incurs storage/obsolescence cost, and can hide inefficiency.',
                'Against: protects against stock-outs, delivery delays and demand spikes; avoids costly lost sales/production halts; vital where supply is unreliable.',
                'Judgement: not a waste if it prevents greater losses; the right buffer balances holding cost against stock-out cost. Depends on supply reliability and demand volatility.',
                'L|Level 4 (10-12)|Balanced, supported judgement.',
                'L|Level 3 (7-9)|Balanced.', 'L|Level 2 (4-6)|Limited.', 'L|Level 1 (1-3)|One-sided.',
            ]),
        ]),
        Q([
            P('a', 'Analyse how a business could interpret an inventory control chart to manage stock.', 8, [
                'Read maximum, re-order and buffer levels; monitor the rate of stock usage.',
                'Identify when to re-order (at re-order level) and spot abnormal usage or delivery delays.',
                'Adjust re-order level/quantity as lead time or demand changes.',
                'L|Level 3 (6-8)|Developed analysis referencing the chart.',
                'L|Level 2 (3-5)|Some.', 'L|Level 1 (1-2)|Identification.',
            ]),
            P('b', 'Evaluate whether building resilience into the supply chain is worth the extra cost.', 12, [
                'For: protects against disruption (pandemics, wars, supplier failure), avoids costly shutdowns/lost sales, protects reputation.',
                'Against: dual-sourcing/extra stock/local suppliers raise costs and reduce JIT savings; disruptions may be rare.',
                'Judgement: increasingly worthwhile given recent global shocks; depends on the likelihood and cost of disruption vs the cost of resilience.',
                'L|Level 4 (10-12)|Balanced, supported judgement.',
                'L|Level 3 (7-9)|Balanced.', 'L|Level 2 (4-6)|Limited.', 'L|Level 1 (1-3)|One-sided.',
            ]),
        ]),
        Q([
            P('a', 'Analyse the factors that determine the re-order level and re-order quantity a business should set.', 8, [
                'Lead time and its reliability; rate of usage/demand and its variability.',
                'Cost of holding vs ordering; storage capacity; supplier discounts and reliability.',
                'Risk/cost of a stock-out.',
                'L|Level 3 (6-8)|Developed analysis.', 'L|Level 2 (3-5)|Some.',
                'L|Level 1 (1-2)|Identification.',
            ]),
            P('b', '\u2018A JIC (Just in Case) approach is safer and therefore always better than JIT.\u2019 Evaluate.', 12, [
                'For JIC: security of supply, no stock-outs, copes with demand spikes and unreliable suppliers.',
                'Against: high holding costs, cash tied up, obsolescence/waste; JIT is cheaper and leaner where supply is reliable.',
                'Judgement: \u2018safer\u2019 but not always \u2018better\u2019 \u2013 depends on cost of holding vs cost of disruption; many firms use a hybrid. Context-dependent.',
                'L|Level 4 (10-12)|Balanced, supported judgement.',
                'L|Level 3 (7-9)|Balanced.', 'L|Level 2 (4-6)|Limited.', 'L|Level 1 (1-3)|One-sided.',
            ]),
        ]),
    ],
    'case': {
        'title': 'Stock trouble at Vela Furniture',
        'context': [
            'Vela Furniture assembles flat-pack furniture. It currently holds large buffer stocks of imported components \u2018just in case\u2019, but storage costs are high and some parts become obsolete when designs change. A consultant recommends moving towards JIT, sourcing more components locally and using an inventory control system with clear re-order levels.',
            'Recently a shipping delay caused a two-week stock-out of a key component, halting one production line. Managers disagree: some want even bigger buffers, others want JIT to free up cash. Vela\u2019s cash flow is tight.',
        ],
        'exhibits': [
            {'type': 'diagram', 'name': 'inventory', 'caption': 'Fig 1: Vela\u2019s inventory control chart for a key component'},
            {'type': 'table', 'title': 'Table 1: Inventory data for a key component',
             'headers': ['Measure', 'Value'],
             'rows': [['Maximum inventory', '4,000 units'],
                      ['Buffer inventory', '800 units'],
                      ['Weekly usage', '1,600 units'],
                      ['Lead time', '1 week'],
                      ['Annual holding cost per unit', '$3']],
             'col_w': [3, 1], 'align': ['left', 'right']},
        ],
        'questions': [
            Q([P('', 'Define the term \u2018lead time\u2019.', 2, ['Time between placing an order and receiving the goods (2).'])]),
            Q([P('', 'Using Table 1, calculate the re-order level for the key component.', 3, [
                '=Re-order level = buffer + (usage during lead time) = 800 + (1,600 \u00d7 1) = 2,400 units',
                '2 method + 1 answer (2,400).',
            ])]),
            Q([P('', 'Using Table 1, estimate the annual holding cost of the buffer inventory.', 3, [
                '=Buffer holding cost \u2248 800 units \u00d7 $3 = $2,400 per year (accept average-stock reasoning if shown).',
                '2 method + 1 answer.',
            ])]),
            Q([P('', 'Explain one drawback Vela is experiencing from holding large buffer stocks.', 4, [
                'High storage costs and cash tied up (tight cash flow), plus obsolescence when designs change.',
                '1\u20132 + development using the case.',
            ])]),
            Q([P('', 'Analyse the risks to Vela of moving to a JIT system after the recent shipping delay.', 8, [
                'JIT removes the buffer that currently protects against delays -> stock-outs would halt lines (as happened) more often.',
                'Relies on reliable, fast local suppliers; imported parts have long, uncertain lead times.',
                'Lost output/sales and idle labour if supply fails; but frees cash and cuts storage/obsolescence.',
                'L|Level 3 (6-8)|Developed analysis of JIT risks using the case.',
                'L|Level 2 (3-5)|Some.', 'L|Level 1 (1-2)|Identification.',
            ])]),
            Q([P('', 'Recommend an inventory strategy for Vela (e.g. full JIT, more local sourcing, or larger buffers). Justify your recommendation using the case and data.', 12, [
                '#Options', 'Full JIT (cuts cost/cash but risky with imports); bigger buffers (secure but costly/obsolescence); hybrid with local sourcing.',
                '#Use of data', 'Tight cash favours cutting stock; but the recent 2-week stock-out shows disruption risk; re-order level 2,400 with buffer 800 is exposed to long import lead times.',
                '#Judgement', 'Supported recommendation, e.g. adopt a hybrid \u2013 source key/at-risk components locally with modest buffers and apply JIT to reliable, low-risk parts; keep a control system with sensible re-order levels. Balances cash pressure against stock-out risk.',
                'L|Level 4 (10-12)|Balanced, uses data, justified recommendation.',
                'L|Level 3 (7-9)|Balanced, some judgement/application.',
                'L|Level 2 (4-6)|Limited.', 'L|Level 1 (1-3)|One-sided/assertion.',
            ])]),
        ],
    },
}
