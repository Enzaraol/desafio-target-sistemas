"""
considerando que posso ir apenas 2 vezes na mesma sala, eu ligaria dois interruptores e iria verificar uma das salas. Se a lâmpada 
estivesse ligada, eu voltaria nos interruptores e desligaria um deles. Caso a luz permanecesse ligada, me sobrariam apenas 2 interruptores
e mais uma ida em outra sala. Assim eu ligaria outro interruptor e visitaria outra sala, constatando se a lâmpada está ligada ou não.
Se estiver ligada eu saberei que o próximo interruptor liga a última sala, se estiver desligada eu sei q esse interruptor ligou a sala 
da qual não visitei e assim eu saberei qual interruptor liga qual sala.

Se a lâmpada estivesse desligada na minha primeira ida a sala, quando eu liguei dois interruptores, eu saberia que o interruptor do qual
eu não acionei acende a lâmpada da sala escura que visitei. E assim me sobrariam apenas 2 interruptores e eu seguiria novamente com a 
lógica acima. Eu ligaria outro interruptor e visitaria outra sala, constatando se a lâmpada está ligada ou não. Se estiver ligada eu saberei que o próximo interruptor liga a última sala, se estiver desligada eu sei q esse interruptor ligou a sala 
da qual não visitei e assim eu saberei qual interruptor liga qual sala.

"""