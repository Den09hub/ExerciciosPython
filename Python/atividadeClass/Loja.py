class Computador:
    gabinete = 'Ausente gabinete'
    monitor = 'Ausente monitor'
    placa_de_video = 'Ausente placa de vídeo'
    disco_rigido = 'Ausente disco rígido'
    processador = 'Ausente processador'

    def pc_detalhes(self):
        print(f'{self.gabinete}')
        print(f'{self.monitor}')
        print(f'{self.placa_de_video}')
        print(f'{self.disco_rigido}')
        print(f'{self.processador}')

computador1 = Computador()
gabinete = 'Gabinete'
monitor = 'Monitor'
placa_de_video = 'Placa de Vídeo'
disco_rigido = 'Disco Rígido'
processador = 'Processador'
computador1.pc_detalhes()

