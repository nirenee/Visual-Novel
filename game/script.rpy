# The script of the game goes in this file.


# DEFINIR PERSONAJES
define D = Character("Director",color="#804000")
define J = Character("Jay",color="#2359D7")
define H = Character("Hina",color="#BF0CC4")
define A = Character("Akira",color ="#FF00DC")
define P = DynamicCharacter("Nombre",color="#F84A35")
#[Nombre] para hacer referencia al nombre del protagonista

$ Nombre = ""
# SPRITES PERSONAJES
image Akira = "chica.png"
image jay_normal = "Protagonista.png"
image jay_feliz = "Protagonista feliz.png"
#DEFINIR SONIDOS
define elegir = "audio/sonidos/elegir.ogg"
define mostrar = "audio/sonidos/mostrar menu.ogg"
define no_elegir = "audio/sonidos/no elegir.ogg"
define pasos = "audio/sonidos/Pasos.ogg"
define puerta = "audio/sonidos/Puerta.ogg"
#DEFINIR CONDICIONES
$ objeto = ""
# The game starts here.

image splash = "Aviso.png"
label splashscreen:
    show splash with fade
    pause
    return

label start:
    $ objeto ="nada"
    "Soy un chico de 18 años, me acabo de graduar de la preparatoria para ir
    a la universidad."
    "Hace poco me mude con mis padres a una nueva zona donde no conozco a nadie,
    espero hacer amigos pronto."
    "¿Por cierto aun no me he presentado verdad?"
    "Mi nombre es:"
    $Nombre = renpy.input("Escribe tu nombre")





    play music "audio/ambiente-normal.mp3"
    scene casa with fade:

    "Mis ojos se sienten pesados...
    me cuesta incorporarme adecuadamente encima de la cama."
    "Cuando voy a ver la hora que es, la pesadez que sentía
    en los parpados desaparece por completo al ver el movil."

    P "¡Mierda llego tarde!"
    play sound pasos

    "Tras salir de mi casa, el sol deslumbra mi vista."
    scene casa prota fuera with fade:
        xzoom 2.5 yzoom 2.25
    P "Tengo que darme prisa o acabaré llegando tarde"
    "El primer dia de clases es importante,
    no puedo saltarme la presentacion como la ultima vez."

    #Se escuchan un sonido de efecto de correr del protagonista
    P "Puedo llegar a tiempo, aun faltan 10 minutos para que comience."
    "Empiezo a correr y al doblar la esquina de la tienda de conveniencia
    un encuentro inesperado sucedió ante mí."
    "Un choque cabeza con cabeza tuvo lugar."
    P "Auch!"
    A "Ay!!"
    "Cierro instintivamente los ojos debido al impacto
    para posteriormente comenzar a abrirlos poco a poco."
    "Al abrir completamente los ojos veo una silueta en el suelo,
    esta silueta la habia visto en alguna parte antes...
    ¡¡Era ella!!"
    show Akira at center with fade:
        xzoom 0.6 yzoom 0.6
        yalign -4
    A"¡¡Oye ten mas cuidado!!"

    "Con una voz áspera pero a la vez fina me decía esas palabras."


    P "Perdona, fue sin querer"
    "Le contesto asumiendo mi parte de culpa."
    "Tras decir eso observo como se le habia caido una especie de bolso."

    $ timeout_label = "escena4"
    play sound mostrar
    menu:
        "Toma":
            P"Perdona, se te ha caido esto"
            play sound elegir
            jump escena2
        "*Abrir el bolso":
            play sound elegir
            jump escena3


label escena2:
    $ timeout_label = None
    #Aumenta un poco el afecto de ella por el prota
    hide Akira with fade
    "Cuando estiro el brazo para dárselo, ella rápidamente lo coge
    y sin siquiera mirarme sigue por su camino."
    "Al menos podría darme las gracias, pienso un poco molesto,
    pero bueno no importa, no tengo tiempo que perder."
    "Cuando prosigo por mi camino, observo que se le habia caido una especie de
    colgante"
    play sound mostrar
    menu:
        "*Coger el colgante":
            play sound elegir
            $ objeto = "colgante"
            jump coger_colgante

label escena3:
    $ timeout_label = None
    #Baja el afecto de ella por el prota
    show Akira at center with fade:
        xzoom 0.6 yzoom 0.6
        yalign -4
    A "Hey que crees que haces!!"
    "Rapidamente se dirige hacia mi y me lo quita de las manos.
    Puedo ver lo enfadada que está por haber hecho eso"
    P"Tranquila solo estaba bromeando"
    "Le digo mientras me toco un poco la cabeza. Tras haberle dicho eso
    ella se dirige hacia el sentido opuesto con bastante urgencia"
    hide Akira with fade
    P"No es momento de estar parado tengo que seguir!!"
    "Tras decirme esas autoproclamadas palabras me dirijo hacia la universidad"
    jump llegar_tarde

label escena4:
        play sound no_elegir
        hide Akira
        $ timeout_label = None
        "No tengo tiempo que perder, tengo que seguir"
        jump entrar_salon
label coger_colgante:
    "Me agacho para coger el colgante, al cogerlo no pude evitar
     ver el reloj de mi muñeca, al verlo rapidamente comenze a correr de nuevo"
    "¡¡No tengo tiempo que perder, voy a llegar tarde!!"
    jump llegar_tarde


#SEGUNDA PARTE
label entrar_salon:
    scene universidad:
        xzoom 1.3 yzoom 1.3
    P"Este año no puedo faltar"
    "Tras correr hasta la puerta del salón de actos, donde se iba a producir
    la charla para todo el alumnado nuevo, me encontraba exhausto y
    practicamente sin fuerza"
    play sound mostrar
    menu:
        "*Entrar al salón de actos":
            play sound elegir
            jump entrar
        "*Decides darte una vuelta por la universidad":
            play sound elegir
            jump dar_vuelta
label llegar_tarde:
        scene fuera_del_salon with dissolve:
            xzoom 1.3 yzoom 1.3
        show jay_normal at center:
            xzoom 0.6 yzoom 0.6
            yalign -4
        J"Hey"
        show jay_feliz at center:
            xzoom 0.6 yzoom 0.6
            yalign -4
        P"¡Jay!"
        P"¡Vamos que nos llegamos a la presentación"
        jump escena_clase
label dar_vuelta:
        scene universidad with dissolve:
            xzoom 1.3 yzoom 1.3
        "Bueno, otro año que me pierdo la charla presencial"
        "Sinceramente no me importa mucho lo que puedan decir pero debo
        centrarme este año ya que los anteriores no me ha ido muy bien"
        "Heyyy"
        "Escucho detras mio, mientras comienzo a darme la vuelta, le contesto
        sin saber quien es"
        #enseñar a la chica nuevamente
        P"Ey que tal"
        "Lo que yo no me esperaba era que fuera a coincidir de nuevo con esta
        persona"
        show Akira at center with fade:
            xzoom 0.6 yzoom 0.6
            yalign -4
        A"Que coincidencia que me vuelva a cruzar contigo aquí"
        play sound mostrar
        menu:
            "*Irte con ella":
                play sound elegir
                jump escena_juntos
            "Te vas a clase":
                play sound elegir
                "Me fui directo hacia clase y me encontre con Jay de camino"
                jump escena_clase



label entrar:
        scene universidad with fade:
            xzoom 1.3 yzoom 1.3
        D"Este año espero que sea muy bueno para todo el alumnado nuevo ya que
        todo esto es nuevo y al principio es dificil de acostumbrarse"
        D"Pero estoy seguro que todos vosotros lograreis todo lo que os
        propongais y tendreis un futuro muy exitoso..."
        #sonido entrar puerta
        play sound puerta
        "En ese mismo momento, entre por la puerta y me percate que había
        interrumpido la charla del director"
        P"Ups, disculpe por la tardanza"
        #sonido abuchear
        "Después del enorme abucheo que recibí de todo el salon de actos,
        busqué mi sitio y me sente hasta que terminó la charla"
        "Una vez que terminó, me reuní con Jay y fuimos juntos a clase"
        show jay_normal at center with fade:
            xzoom 0.6 yzoom 0.6
            yalign -4
        J"Ostia tio, como la has liado"
        J"!Como entras a mitad de la charla del director¡"
        hide jay_normal
        show jay_feliz at center with fade:
            xzoom 0.6 yzoom 0.6
            yalign -4
        P"Jajajajaja no tenía ni idea"
        play sound pasos
        jump escena_clase
label escena_clase:
    scene clase with fade:
        xzoom 1.3 yzoom 1.3
    "Claramente no llegamos a tiempo a la presentación y fuimos directos
    a la siguiente clase, ya que Jay y yo ibamos juntos."
    "Para mi Jay era como un hermano ya que lo conocía desde pequeño, y
    decidí contarle lo que me paso esta mañana con la chica con la cual
    tropecé"
    show jay_feliz at center with fade:
        xzoom 0.6 yzoom 0.6
        yalign -4
    J"Pero que dices tio jajajajajja"
    J"Por poco la matas de la ostia que le diste seguro"
    P"Tampoco te pases,Jay"
    "Después de contarle brevemente lo ocurrido, me di cuenta que a pesar
    de no conocerla casi, quería estar con ella"
    P"Jay, creo que me gusta la chica de esta mañana, quiero volver a verla"
    J"Eso es imposible, nunca más la vas a volver a ver"
    J"Esta tarde quieres venirte a jugar un partido?"
    P"Claro ti...."
    "En ese mismo momento por casualidad mire por la puerta y..."
    "!!Era ella¡¡ Estaba justo pasando por el pasillo donde tenía clases"
    play sound mostrar
    menu:
        "*Te levantas y vas corriendo a hablar con ella":
            play sound elegir
            P"Lo siento tio, esta tarde no puedo, voy al baño!!"
            hide jay_feliz
            show jay_normal at center with fade:
                xzoom 0.6 yzoom 0.6
                yalign -4
            "Le dije apresuradamente, estas palabras soprendieron a Jay, el cual me vio
            saliendo de clases sin decir ni una palabra"
            J"....."
            jump escena_pasillo
        "*A pesar que la ves no haces nada porque piensas que resultará inutil":
            play sound elegir
            "...."
            J"bro?"
            P"A si nada, perdona, que decias?"
            J"Si te querias venir esta tarde a jugar un partido de futbol"
            P"Ah, claro"
            jump escena_salida_universidad


label escena_juntos:
    "Después de caminar y estar hablando durante un rato terminamos en la
    azotea del edificio en el cual teniamos clase"
    scene azotea with fade:
        xzoom 1.3 yzoom 1.3
    "Tras haber estado tanto tiempo con ella ese mismo dia me di cuenta que
    realmente me gustaba la chica y quería estar con ella"
    P"Oye, tengo que decirte una cosa..."
    jump escena_declaracion

#TERCERA PARTE
label escena_pasillo:
    scene pasillo with fade:
        xzoom 1.3 yzoom 1.3
    if objeto == "colgante":
        P"¡Perdona!, perdón por molestarte de nuevo pero queria devolverte esto"
        "Le extiendo la mano devolviendole el colgante que se le habia caido"
        P"Esto es tuyo verdad?"
        A"!?, muchas gracias, lo estaba buscando desesperadamente."
        "Me hace un poco feliz escuchar ese comentario"
        A"Dejame que te agradezca como es debido, que te parece si te vienes
        conmigo y mis amigos esta tarde a tomar algo?"
        "!?, en serio?, me esta invitando??, detras de la chica puedo observar
        la silueta de jay, que deberia hacer?"
        show Akira at right:
            xzoom 0.6 yzoom 0.6
            yalign -4
        show jay_normal at left:
            xzoom 0.6 yzoom 0.6
            yalign -4
        play sound mostrar
        menu:
            "Lo siento, pero tengo planes":
                play sound elegir
                A"Ah bueno, no pasa nada, ya te lo agradeceré en otro momento"
                P"Lo siento de verdad"
                "Tras decir estas palabas, me dirijo de nuevo a clase, no puedo
                traicionar a mi amigo"
                P"Hey Jay, pensandolo mejor esta tarde si que voy con vosotros
                a jugar un partido"
                J"jaja, a que se debe este cambio?"
                P"Nada, simplemente me lo he pensado mejor ajajaj"
                scene black with fade
                show text "FINAL#5: EL PARTIDO"
                pause
            "Claro, me encantaría":
                play sound elegir
                "Tras decir eso pude observar la expresion de Jay a lo lejos,
                le he traicionado...."
                "Tras acabar las clases me fui con ella y sus amigos a pasar la
                tarde por ahi"
                "Lo siento Jay pero hay cosas que son mas importantes que la amistad,
                deberias saberlo"
                scene black with fade
                show text"FINAL#4: AMOR>AMISTAD"
                pause
    else:
        P"¡Perdona!, perdón por molestarte de nuevo pero queria saber si esta tarde
        estabas libre"
        "Dije estas palabras exhausto tras haber corrido hasta donde se encontraba."
        "Lo que no me esperaba, era la repuesta que iba a tener en ese
        mismo momento, la cual me destruyó por dentro."
        show Akira at center with fade:
            xzoom 0.6 yzoom 0.6
            yalign -4
        A"Ehhh, creo que te has confundido."
        A"Tu y yo no nos conocemos."
        "Esas palabras quedaron grabadas en mi cabeza."
        "Todas las expectativas e ilusiones que tenía fueron tiradas a la basura
        en ese precio instante."
        "Fue como una puñalada por la espalda"
        P"Ah, bueno..."
        P"Me habré equivocado entonces."
        P"Lo siento."
        "Después de esta escena ridícula la cual, se había enterado todo el pasillo
        volví a clase rodeado de burlas, donde me estaba esperando Jay"
        "Jay se había cabreado conmigo ya que lo había dejado tirado"
        show jay_normal at center with fade:
            xzoom 0.6 yzoom 0.6
            yalign -4
        J"¿¿¿¿Pero qué haces tio?????"
        J"¿No decias que hoy no podias quedar?"
        J"Me has decepcionado"
        "Ese mismo día no perdía a la que pensaba que era el amor de mi vida,
        sino que perdí a un preciado amigo también"
        scene black with fade
        show text"FINAL#1: FOREVER ALONE"
        pause


    return
    #fin
label  escena_salida_universidad:
    hide jay_feliz
    "A pesar de haberla visto, no fui capaz de ir a hablar con ella"
    "Tenía claro que no iba a servir para nada"
    scene fuera_del_salon with fade:
        xzoom 1.3 yzoom 1.3
    "Pasó el día como cualquier otro"
    "Todas las clases aburridas y sin ánimo ya que no fui capaz de hablar con
    ella"
    "Me junté con Jay fuimos juntos para casa ya que vivía cerca mía"
    P"Jay, antes he visto a la chica de la cual te hablé y no he sido capaz
    de hablar con ella"
    P"Me siento un inútil"
    "Jay tras escuchar esto intentó ayudarme todo lo que pudo, ya que siempre
    había estado para mí"
    show jay_feliz at center with fade:
        xzoom 0.6 yzoom 0.6
        yalign -4
    J"No te preocupes, algún día encontrarás a alguien adecuado a ti"
    J"Y seguro que saldrá bien"
    J"Simplemente por ahora no le des muchas vueltas"
    J"Y que a pesar de eso siempre me vas a tener a mi, pase lo que pase"
    "Esas palabras de Jay me sirvieron de mucho ya que me di cuenta de lo
    importante que siempre fue para mí y que siempre ibamos a estar juntos"
    "Ese día no pude estar con el que pensaba que iba a ser el amor de mi vida
    pero me di cuenta de que ya tenía lo que necesitaba a mi lado"
    "Mi mejor amigo, Jay"
    scene black with fade
    show text"FINAL#2: LOS MEJORES AMIGOS "
    pause
    return
label escena_declaracion:
    play music "audio/Time Flow"
    scene azotea with fade:
        xzoom 1.3 yzoom 1.3
    P"Bueno, llevo pensándolo todo el día y a pesar de haber coincidido
    muy poco y apenas haber tenido contecto"
    P"Creo que congeniamos mucho y que podríamos llegar a algo... nose"
    show Akira at center with fade:
        xzoom 0.6 yzoom 0.6
        yalign -4
    A"Pero, que dices"
    A"¿A que te refieres?"
    P"Si, bueno... ya sabes a lo que me refiero"
    A"No te entiendo, habla claro"
    P"¡Pues que me gustas!"
    P"A pesar del poco tiempo que hemos vivido solo quiero estar contigo"
    P"Desde el primer encuentro fortuito esta mañana no he dejado de pensar
    en ti"
    P"Fue amor a primera vista"
    A"... Todo esto es muy repentino de repente nose..."
    A"No sabría que decirte ahora mismo..."
    "Tras esa respuesta de ella, perdí en parte la esperanza de que me diera
    una oportunidad"
    "Sabía claramente que todo había pasado muy rápido, pero podía esconder
    los sentimientos que sentía en ese momento"
    "No me arrepentía de nada"
    "Pero sucedió lgo inesperado..."
    "Justo cuando iba a despedirme ya que pensaba que me había rechazado
    me dijo esto"
    A"A pesar de no saber que responder ahora mismo, es cierto que hemos estado
    muy bien hoy"
    A"Me gustaría seguir contigo para ver que sucede entre nosotros, ya que
    aun es muy pronto y a futuro darte una respuesta final"
    "!En ese momento me puse muy feliz, era la persona mas feliz del mundo!"
    P"!Vale, de acuerdo me parece perfecto¡"
    "Después de lo sucedido fui corriendo a clase a explicarle toda la
    situación a mi amigo Jay y ponerle al día de todo"
    "El me apoyo en todo como de costumbre y lo aprecio todo"
    "Desde ese día nuestra relación fue a mejor hasta el día de hoy en que
    por fin empezamos a salir"
    scene black with fade
    show text"FINAL#3: A LARGO PLAZO"
    pause
    return
