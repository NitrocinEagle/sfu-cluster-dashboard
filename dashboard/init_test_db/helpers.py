__author__ = 'mist'
from dashboard.app.models import LineChartMetric, PieChartMetric

PRINT = False

def get_dataset(graph_type, metric):
    dataset = []
    if graph_type is 'line_chart':
        for data_point in metric:
            if PRINT:
                print 'new_point: '
            new_point = LineChartMetric(
                timestamp=data_point['timestamp'],
                value=data_point['value']
            )
            if PRINT:
                print '\ttimestamp: ', new_point.timestamp
                print '\tvalue: ', new_point.value
            dataset.append(new_point)
        return dataset
    if graph_type is 'pie_chart':
        for sector in metric:
            if PRINT:
                print 'sector: ', sector
            new_sector = PieChartMetric()
            new_sector.timestamp = sector['timestamp']
            new_sector.data = []
            if PRINT:
                print 'new_sector: '
                print '\ttimestamp: ', new_sector.timestamp
                print '\tsector_data: '
            for sector_data in sector['data']:
                new_sector_data = new_sector.SectorData(
                    sector_name=sector_data['sector_name'],
                    value=round(sector_data['value'], 2)
                )
                if PRINT:
                    print '\t\tname: ', new_sector_data.sector_name
                    print '\t\tvalue: ', new_sector_data.value
                new_sector.data.append(new_sector_data)
            dataset.append(new_sector)
        return dataset
    return None