// Timer de Foco (Pomodoro simples) no TM1637
// Autor: Venicio

#include <TM1637Display.h>

const int PIN_CLK = 3;
const int PIN_DIO = 4;
const int PIN_BTN = 2;

// 25 segundos para teste (no real seria 25*60)
const int FOCUS_SECONDS = 25*60;

TM1637Display display(PIN_CLK, PIN_DIO);

bool rodando = false;
int tempoRestante = FOCUS_SECONDS;
unsigned long ultimoTick = 0;
bool ultimoEstadoBotao = HIGH;

void setup() {
  pinMode(PIN_BTN, INPUT_PULLUP);

  display.setBrightness(0x0f); // brilho maximo
  mostrarTempo(tempoRestante);
}

// Mostra MM:SS no display
void mostrarTempo(int segundos) {
  int min = segundos / 60;
  int seg = segundos % 60;

  int valor = min * 100 + seg; // ex: 1 min 23 -> 0123

  // 0b01000000 liga os dois-pontos
  display.showNumberDecEx(valor, 0b01000000, true);
}

void loop() {
  bool leitura = digitalRead(PIN_BTN);

  // Clique no botao (bordo HIGH -> LOW)
  if (leitura == LOW && ultimoEstadoBotao == HIGH) {
    // alterna estado
    rodando = !rodando;

    // se parou, reseta o tempo
    if (!rodando) {
      tempoRestante = FOCUS_SECONDS;
      mostrarTempo(tempoRestante);
    } else {
      // iniciou contagem
      ultimoTick = millis();
    }

    delay(150); // debounce
  }
  ultimoEstadoBotao = leitura;

  if (rodando) {
    unsigned long agora = millis();
    if (agora - ultimoTick >= 1000) { // 1 segundo
      ultimoTick = agora;

      if (tempoRestante > 0) {
        tempoRestante--;
        mostrarTempo(tempoRestante);
      } else {
        // acabou o tempo de foco -> pisca display
        for (int i = 0; i < 6; i++) {
          display.clear();
          delay(200);
          mostrarTempo(0);
          delay(200);
        }
        // prepara para novo ciclo
        rodando = false;
        tempoRestante = FOCUS_SECONDS;
        mostrarTempo(tempoRestante);
      }
    }
  }
}
