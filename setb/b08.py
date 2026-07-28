from ._model import P, Q

PAPER = {
    'code': 'B8',
    'title': 'Operations management (Syllabus 4)',
    'theme': 'Knowledge recall: the transformation process, efficiency/productivity/sustainability, production methods, inventory, JIT, capacity utilisation and outsourcing.',
    'time': '35 minutes',
    'questions': [
        Q([
            P('a', 'Define the \u2018transformational process\u2019.', 2, ['Converting inputs (resources) into outputs (goods/services) (1) that have greater value (1).']),
            P('b', 'State what is meant by \u2018inputs\u2019 and \u2018outputs\u2019.', 2, ['Inputs: resources used (land, labour, capital) (1); outputs: the finished goods/services produced (1).']),
        ]),
        Q([
            P('a', 'Distinguish between efficiency and effectiveness.', 2, ['Efficiency: producing with least waste/cost (1); effectiveness: achieving the intended objective/meeting needs (1).']),
            P('b', 'Define \u2018productivity\u2019.', 1, ['Output per unit of input in a given time (1).']),
            P('c', 'Define \u2018sustainability\u2019 in operations.', 1, ['Producing without harming the environment/future generations\u2019 needs (1).']),
        ]),
        Q([
            P('a', 'Define \u2018labour productivity\u2019.', 2, ['Output per worker (1) in a given period (1).']),
            P('b', 'State the formula for labour productivity.', 2, ['Total output / number of workers (2).']),
        ]),
        Q([
            P('a', 'Distinguish between capital-intensive and labour-intensive operations.', 2, ['Capital-intensive: relies mainly on machinery/technology (1); labour-intensive: relies mainly on human effort (1).']),
            P('b', 'State one benefit of capital-intensive production.', 1, ['Consistent quality, high output/low unit cost, works continuously (1).']),
            P('c', 'State one benefit of labour-intensive production.', 1, ['Flexible, suits bespoke/craft work, lower capital cost (1).']),
        ]),
        Q([
            P('a', 'Define \u2018job production\u2019.', 2, ['Producing one-off/custom items individually (1) to a customer\u2019s specific requirements (1).']),
            P('b', 'Define \u2018batch production\u2019.', 2, ['Producing groups (batches) of identical products (1) that move through each stage together (1).']),
        ]),
        Q([
            P('a', 'Define \u2018flow production\u2019.', 2, ['Continuous mass production of standardised products (1) on a production line (1).']),
            P('b', 'Define \u2018mass customisation\u2019.', 2, ['Using flexible production (1) to make large volumes of individually tailored products at near mass-production cost (1).']),
        ]),
        Q([
            P('a', 'State one advantage of job production.', 1, ['Meets exact needs, premium price, high quality (1).']),
            P('b', 'State one advantage of flow production.', 1, ['Low unit cost at volume, consistent quality (1).']),
            P('c', 'State one problem of changing from batch to flow production.', 1, ['High investment, retraining, downtime, loss of flexibility (1).']),
        ]),
        Q([
            P('', 'State the three types of inventory held by a manufacturer.', 3, ['Raw materials, work in progress, finished goods (1 each).']),
        ]),
        Q([
            P('a', 'Define \u2018buffer inventory\u2019.', 2, ['A minimum level of stock held as a safety margin (1) to cover unexpected demand or delivery delays (1).']),
            P('b', 'Define \u2018lead time\u2019.', 1, ['The time between placing an order and receiving the goods (1).']),
            P('c', 'Define \u2018re-order level\u2019.', 1, ['The stock level at which a new order is placed (1).']),
        ]),
        Q([
            P('a', 'State two costs of holding inventory.', 2, ['Any two: storage, insurance, obsolescence/spoilage, cash tied up (1 each).']),
            P('b', 'State two benefits of holding inventory.', 2, ['Any two: meets unexpected demand, avoids stock-outs, buffers delays, bulk discounts (1 each).']),
        ]),
        Q([
            P('a', 'Define \u2018Just in Time (JIT)\u2019.', 2, ['An approach where materials arrive exactly when needed (1), minimising stock held (1).']),
            P('b', 'Define \u2018Just in Case (JIC)\u2019.', 2, ['Holding buffer stock \u2018just in case\u2019 (1) to protect against demand/supply fluctuations (1).']),
        ]),
        Q([
            P('a', 'State one benefit of JIT.', 1, ['Lower holding costs, less cash tied up, less waste (1).']),
            P('b', 'State one risk of JIT.', 1, ['Vulnerable to supply disruption/stock-outs (1).']),
            P('c', 'State one requirement for JIT to work.', 1, ['Reliable suppliers, frequent deliveries, accurate forecasting (1).']),
        ]),
        Q([
            P('a', 'Define \u2018supply chain management\u2019.', 2, ['Managing the flow of materials, goods and information (1) from suppliers through production to the customer (1).']),
            P('b', 'State one benefit of effective supply chain management.', 1, ['Lower costs/lead times, reliable supply, better quality/service (1).']),
        ]),
        Q([
            P('a', 'Define \u2018capacity utilisation\u2019.', 2, ['The percentage of maximum possible output (1) currently being used (1).']),
            P('b', 'State the formula for capacity utilisation.', 2, ['(Current output / maximum possible output) \u00d7 100 (2).']),
        ]),
        Q([
            P('a', 'State one problem of operating at very low capacity utilisation.', 1, ['High fixed cost per unit, idle resources, low profit (1).']),
            P('b', 'State one problem of operating at (or above) full capacity for long.', 1, ['No slack for orders/maintenance, overworked staff/machines, quality falls (1).']),
            P('c', 'State one way to improve low capacity utilisation.', 1, ['Increase demand (marketing), rationalise capacity, subcontract for others (1).']),
        ]),
        Q([
            P('a', 'Define \u2018rationalisation\u2019.', 2, ['Reducing capacity/resources (1) to cut costs and raise efficiency/utilisation (1).']),
            P('b', 'State why higher capacity utilisation lowers unit costs.', 2, ['Fixed costs are spread over more units (1), reducing fixed cost per unit (1).']),
        ]),
        Q([
            P('a', 'Define \u2018outsourcing\u2019.', 2, ['Contracting a business activity out to an external provider (1) rather than doing it in-house (1).']),
            P('b', 'State one benefit of outsourcing.', 1, ['Lower cost, specialist expertise, flexibility, focus on core (1).']),
            P('c', 'State one drawback of outsourcing.', 1, ['Less control over quality/timing, reliance on supplier, reputation risk (1).']),
        ]),
        Q([
            P('a', 'State two measures that could improve the sustainability of operations.', 2, ['Any two: recycle/reduce waste, energy-efficient equipment, renewable energy, sustainable materials (1 each).']),
            P('b', 'State one benefit to a business of more sustainable operations.', 1, ['Lower long-run costs, better reputation, meets regulation/customer demand (1).']),
        ]),
        Q([
            P('a', 'State one way to increase a business\u2019s capacity.', 1, ['Invest in machinery/premises, hire staff, add shifts/overtime, outsource (1).']),
            P('b', 'State how productivity and unit costs are linked.', 2, ['Higher productivity lowers labour/variable cost per unit (1), reducing average cost (1).']),
        ]),
        Q([
            P('a', 'State how added value is created in operations.', 2, ['Efficient transformation of inputs into outputs (1) worth more than the input cost (1).']),
            P('b', 'State one way to read an inventory control chart.', 2, ['Identify maximum, re-order and buffer levels (1) and when stock hits the re-order level (1).']),
        ]),
    ],
}
