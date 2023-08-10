class contaCorrete:
    def _init_(self):
        self._saldo = None

    def depositar(self, valor):  #referente ao SET  
        self._saldo += valor

    def consultar_saldo(self):  #referente ao GET
        return self._sald        