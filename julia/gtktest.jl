using Gtk


win = GtkWindow("GTK Program", 360, 130)
b = GtkButton("Click")
push!(win,b)

showall(win)

# Not sure what it does.
if !isinteractive()
    c = Condition()
    signal_connect(win, :destroy) do widget
        notify(c)
    end
    @async Gtk.gtk_main()
    wait(c)
end