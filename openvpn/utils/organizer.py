from datetime import datetime


def organize_status(function):
    # Função decorator que ajusta os dados.
    def get_bytes(data):
        # Converte os valor de dados trafegado.
        data = int(data)
        info = ['b', 'Kb', 'Mb', 'Gb', 'Tb']
        count = 0
        while data > 1024:
            data = data / 1024
            count += 1
        return str(round(data, 2)) + info[count]

    def get_time(date_x, date_y):
        # Ajusta as data e horario para retornar o total de tempo logado no sistema.
        date_x = datetime.strptime(date_x, "%Y-%m-%d %H:%M:%S")
        date_y = datetime.strptime(date_y, "%Y-%m-%d %H:%M:%S")
        return str(date_y - date_x)

    def organaze_data(data):
        # Disponibiliza todos os dados ajustados na sequencia correta.
        del data[6]
        del data[6]
        data[2] = get_bytes(data[2])
        data[3] = get_bytes(data[3])
        data.append(get_time(data[4], data[6]))
        return data

    def create_dict(index, value):
        # Cria um dicionario para cada usuario conectado no sistema
        connected = []
        for logged in value:
            user = {}
            for ind in range(len(index)):
                user[index[ind].lower().replace(" ", "_")] = logged[ind]
            connected.append(user)
        return connected

    def get_logged(*args, **kwargs):
        data = function(*args, **kwargs).split("ROUTING TABLE\r\n")
        data_x = data[0].replace("\r", "").split("\n")[2:]
        data_x = data_x[:-1]
        data_y = data[1].replace("\r", "").split("\n")[:-4]
        data_list = [str(data_x[0] + ',' + data_y[0]).split(',')]
        for a in data_x:
            if "." in a:
                c = a.split(',')
                for b in data_y:
                    if c[0] in b:
                        d = a + ',' + b
                        data_list.append(d.split(','))
        del data_list[0][6]
        del data_list[0][6]
        data_list[0].append('how_long')
        data_index = data_list[0]
        data_value = []
        for base in data_list[1:]:
            data_value.append(organaze_data(base))
        return create_dict(data_index, data_value)
    return get_logged


def organize_log(function):
    def convert_timestamp(data):
        date = datetime.fromtimestamp(int(data))
        return datetime.strftime(date, "%Y-%m-%d %H:%M:%S")

    def classification(data):
        if data:
            log_level = {
                'F': 'FATAL',
                'N': 'ERROR',
                'W': 'WARN',
                'I': 'INFO',
                'D': 'DEBUG'
            }
            return log_level[data]
        else:
            return ''

    def get_log(*args, **kwargs):
        data = function(*args, **kwargs).split('\r\n')
        data.pop()
        data.pop()
        data_index = ['when', 'flag', 'msg']
        data_value = []

        for info in data:
            info = info.split(',')
            data_value.append([convert_timestamp(info[0]), classification(info[1]), ', '.join(info[2:])])

        log_dict = []
        for info in data_value:
            log = {}
            for index in range(len(data_index)):
                log[data_index[index]] = info[index]
            log_dict.append(log)

        return log_dict
    return get_log


def organize_state(function):
    def convert_timestamp(data):
        date = datetime.fromtimestamp(int(data))
        return datetime.strftime(date, "%Y-%m-%d %H:%M:%S")

    def how_lonf(data):
        return str(datetime.today() - datetime.fromtimestamp(int(data)))

    def get_state(*args, **kwargs):
        data = function(*args, **kwargs).split('\r\n')[0].split(',')[:4]
        data_dict = {
            'when': convert_timestamp(data[0]),
            'state': data[1],
            'type': data[2],
            'ip_address': data[3],
            'how_long': how_lonf(data[0])
        }
        return data_dict
    return get_state
