import turtle as t

def box(x,y,colour):
    rb.goto(x,y)
    rb.color(f"{colour}")
    rb.down()
    rb.begin_fill()
    for i in range (4):
        rb.fd(column)
        rb.lt(90)
    rb.end_fill()    
    rb.up()    
rb=t.Turtle()
rb.up()
rb.speed(0)
rb.hideturtle()
t.hideturtle()
x=-325
m=x
y=-300
column=80
dp=t.getscreen()
dp.screensize(500,500)
dp.bgcolor("grey")

dp.register_shape("wk.gif")
dp.register_shape("wq.gif")
dp.register_shape("wh.gif")
dp.register_shape("wr.gif")
dp.register_shape("wp.gif")
dp.register_shape("wb.gif")
dp.register_shape("bk.gif")
dp.register_shape("bq.gif")
dp.register_shape("bh.gif")
dp.register_shape("br.gif")
dp.register_shape("bp.gif")
dp.register_shape("bb.gif")

right=0
up=0
colourcolumn=False
count=0
colourarr=["white","brown"]
while up<8*column:
    if colourcolumn==True:
        colour=colourarr[0]
        colourcolumn=False
    else:
        colour=colourarr[-1]
        colourcolumn=True    
    box(x,y,colour)
    count+=1
    if(right>6*column):
        x=m
        y+=column
        up+=column
        right=0
        count+=1
        if colourcolumn==False:
            colourcolumn=True
    else:
        right+=column
        x+=column
    if count%2==0:
        colourcolumn=False
        
writer = t.Turtle()
writer.hideturtle()
writer.penup()
writer.goto(275-60,-340) 
writer.write('Champion (1600)')
writer.pendown()
writer.penup()
writer.goto(-285+12,350)
writer.pendown()
writer.write('Opponent (1600)')
writer.penup()
writer.goto(-325+7,-315)
writer.pendown()
writer.write('a')
writer.penup()
writer.goto(-245+7,-315)
writer.pendown()
writer.write('b')
writer.penup()
writer.goto(-165+7,-315)
writer.pendown()
writer.write('c')
writer.penup()
writer.goto(-85+7,-315)
writer.pendown()
writer.write('d')
writer.penup()
writer.goto(-5+7,-315)
writer.pendown()
writer.write('e')
writer.penup()
writer.goto(75+7,-315)
writer.pendown()
writer.write('f')
writer.penup()
writer.goto(155+7,-315)
writer.pendown()
writer.write('g')
writer.penup()
writer.goto(235+7,-315)
writer.pendown()
writer.write('h')
writer.penup()
writer.goto( -325-15,-300+9)
writer.write('1')
writer.penup()
writer.goto(-325-15,-211)
writer.pendown()
writer.write('2')
writer.penup()
writer.goto(-325-15, -131)
writer.write('3')
writer.penup()
writer.goto(-325-15,-51)
writer.pendown()
writer.write('4')
writer.penup()
writer.goto(-325-15, 29)
writer.write('5')
writer.penup()
writer.goto(-325-15, 109)
writer.write('6')
writer.penup()
writer.goto(-325-15,189)
writer.pendown()
writer.write('7')
writer.penup()
writer.goto(-325-15, 269)
writer.write('8')
writer.penup()

# White Rook 2
wr2 = t.Turtle()
wr2.shape('wr.gif')
wr2.penup()
wr2.setpos(-285,-260)
wr2.ondrag(wr2.goto)

# White Knight 2
wk2 = t.Turtle()
wk2.shape('wh.gif')
wk2.penup()
wk2.setpos(-205,-260)
wk2.ondrag(wk2.goto)

# White Bishop 2
wb2 = t.Turtle()
wb2.shape('wb.gif')
wb2.penup()
wb2.setpos(-125,-260)
wb2.ondrag(wb2.goto)

# White Queen
wq = t.Turtle()
wq.shape('wq.gif')
wq.penup()
wq.setpos(-45,-260)
wq.ondrag(wq.goto)

# White King
wk = t.Turtle()
wk.shape('wk.gif')
wk.penup()
wk.setpos(35,-260)
wk.ondrag(wk.goto)

# White Bishop 2
wb2 = t.Turtle()
wb2.shape('wb.gif')
wb2.penup()
wb2.setpos(115,-260)
wb2.ondrag(wb2.goto)


# White Knight 1
wk1 = t.Turtle()
wk1.shape('wh.gif')
wk1.penup()
wk1.setpos(195,-260)
wk1.ondrag(wk1.goto)

# White Rook 1
wr1 = t.Turtle()
wr1.shape('wr.gif')
wr1.penup()
wr1.setpos(275,-260)
wr1.ondrag(wr1.goto)

# White Pawn 8
wp8 = t.Turtle()
wp8.shape('wp.gif')
wp8.penup()
wp8.setpos(-285,-180)
wp8.ondrag(wp8.goto)

# White Pawn 7
wp7 = t.Turtle()
wp7.shape('wp.gif')
wp7.penup()
wp7.setpos(-205,-180)
wp7.ondrag(wp7.goto)

# White Pawn 6
wp6 = t.Turtle()
wp6.shape('wp.gif')
wp6.penup()
wp6.setpos(-125,-180)
wp6.ondrag(wp6.goto)

# White Pawn 5
wp5 = t.Turtle()
wp5.shape('wp.gif')
wp5.penup()
wp5.setpos(-45,-180)
wp5.ondrag(wp5.goto)

# White Pawn 4
wp4 = t.Turtle()
wp4.shape('wp.gif')
wp4.penup()
wp4.setpos(35,-180)
wp4.ondrag(wp4.goto)

# White Pawn 3
wp3 = t.Turtle()
wp3.shape('wp.gif')
wp3.penup()
wp3.setpos(115,-180)
wp3.ondrag(wp3.goto)

# White Pawn 2
wp2 = t.Turtle()
wp2.shape('wp.gif')
wp2.penup()
wp2.setpos(195,-180)
wp2.ondrag(wp2.goto)

# White Pawn 1
wp1 = t.Turtle()
wp1.shape('wp.gif')
wp1.penup()
wp1.setpos(275,-180)
wp1.ondrag(wp1.goto)

# Black Pawn 8
bp8 = t.Turtle()
bp8.shape('bp.gif')
bp8.penup()
bp8.setpos(-285,220)
bp8.ondrag(bp8.goto)

# Black Pawn 7
bp7 = t.Turtle()
bp7.shape('bp.gif')
bp7.penup()
bp7.setpos(-205,220)
bp7.ondrag(bp7.goto)

# Black Pawn 6
bp6 = t.Turtle()
bp6.shape('bp.gif')
bp6.penup()
bp6.setpos(-125,220)
bp6.ondrag(bp6.goto)

# Black Pawn 5
bp5 = t.Turtle()
bp5.shape('bp.gif')
bp5.penup()
bp5.setpos(-45,220)
bp5.ondrag(bp5.goto)

# Black Pawn 4
bp4 = t.Turtle()
bp4.shape('bp.gif')
bp4.penup()
bp4.setpos(35,220)
bp4.ondrag(bp4.goto)


# Black Pawn 3
bp3 = t.Turtle()
bp3.shape('bp.gif')
bp3.penup()
bp3.setpos(115,220)
bp3.ondrag(bp3.goto)

# Black Pawn 2
bp2 = t.Turtle()
bp2.shape('bp.gif')
bp2.penup()
bp2.setpos(195,220)
bp2.ondrag(bp2.goto)

# Black Pawn 1
bp1 = t.Turtle()
bp1.shape('bp.gif')
bp1.penup()
bp1.setpos(275,220)
bp1.ondrag(bp1.goto)

# Black Rook 2
br2 = t.Turtle()
br2.shape('br.gif')
br2.penup()
br2.setpos(-285,300)
br2.ondrag(br2.goto)

# Black Knight 2
bk2 = t.Turtle()
bk2.shape('bh.gif')
bk2.penup()
bk2.setpos(-205,300)
bk2.ondrag(bk2.goto)

# Black Bishop 2
bb2 = t.Turtle()
bb2.shape('bb.gif')
bb2.penup()
bb2.setpos(-125,300)
bb2.ondrag(bb2.goto)

# Black Queen
bq = t.Turtle()
bq.shape('bq.gif')
bq.penup()
bq.setpos(-45,300)
bq.ondrag(bq.goto)

# Black King
bk = t.Turtle()
bk.shape('bk.gif')
bk.penup()
bk.setpos(35,300)
bk.ondrag(bk.goto)

# Black Bishop 1
bb1 = t.Turtle()
bb1.shape('bb.gif')
bb1.penup()
bb1.setpos(115,300)
bb1.ondrag(bb1.goto)

# Black Knight 1
bk1 = t.Turtle()
bk1.shape('bh.gif')
bk1.penup()
bk1.setpos(205,300)
bk1.ondrag(bk1.goto)

# Black Rook 1
br1 = t.Turtle()
br1.shape('br.gif')
br1.penup()
br1.setpos(275,300)
bk1.ondrag(bk1.goto)

dp.mainloop()