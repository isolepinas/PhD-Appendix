load tempos.mat
xmin=25;
xmax=250;

bins=25;

tiledlayout(6,4)
 
%casals 1
nexttile
y = Casalsrec19301939;
y = add_noise(y);
hist(y, bins)
[heights,centers] = hist(y, bins);
hold on
ax = gca;
ax.XTickLabel = [];
n = length(centers);
w = centers(2)-centers(1);
t = linspace(centers(1)-w/2,centers(end)+w/2,n+1);
p = fix(n/2);
% fill(t([p p p+1 p+1]),[0 heights([p p]),0],'w')
% plot(centers([p p]),[0 heights(p)],'r:')
% h = text(centers(p)-.2,heights(p)/2,'   h');
% dep = -70;
% tL = text(t(p),dep,'L');
% tR = text(t(p+1),dep,'R');
hold off
dt = diff(t);
Fvals = cumsum([0,heights.*dt]);
F = spline(t, [0, Fvals, 0]);
DF = fnder(F);  % computes its first derivative
% h.String = 'h(i)';
% tL.String = 't(i)';
% tR.String = 't(i+1)';
hold on
fnplt(DF, 'r', 2)
hold off
ylims = ylim; 
ylim([0,ylims(2)]);
xlim([xmin xmax])
title('Casals 1930')
xticklabels('auto')
xticks(0:25:400)


%Fournier 1
nexttile
y = Fournierrec194748;
y = add_noise(y);
hist(y, bins)
[heights,centers] = hist(y, bins);
hold on
ax = gca;
ax.XTickLabel = [];
n = length(centers);
w = centers(2)-centers(1);
t = linspace(centers(1)-w/2,centers(end)+w/2,n+1);
p = fix(n/2);
% fill(t([p p p+1 p+1]),[0 heights([p p]),0],'w')
% plot(centers([p p]),[0 heights(p)],'r:')
% h = text(centers(p)-.2,heights(p)/2,'   h');
% dep = -70;
% tL = text(t(p),dep,'L');
% tR = text(t(p+1),dep,'R');
hold off
dt = diff(t);
Fvals = cumsum([0,heights.*dt]);
F = spline(t, [0, Fvals, 0]);
DF = fnder(F);  % computes its first derivative
% h.String = 'h(i)';
% tL.String = 't(i)';
% tR.String = 't(i+1)';
hold on
fnplt(DF, 'r', 2)
hold off
ylims = ylim; 
ylim([0,ylims(2)]);
xlim([xmin xmax])
title('Fournier 1947')
xticklabels('auto')
xticks(0:25:400)


%Tortelier
nexttile
y = Tortelierrec1952;
y = add_noise(y);
hist(y, bins)
[heights,centers] = hist(y, bins);
hold on
ax = gca;
ax.XTickLabel = [];
n = length(centers);
w = centers(2)-centers(1);
t = linspace(centers(1)-w/2,centers(end)+w/2,n+1);
p = fix(n/2);
% fill(t([p p p+1 p+1]),[0 heights([p p]),0],'w')
% plot(centers([p p]),[0 heights(p)],'r:')
% h = text(centers(p)-.2,heights(p)/2,'   h');
% dep = -70;
% tL = text(t(p),dep,'L');
% tR = text(t(p+1),dep,'R');
hold off
dt = diff(t);
Fvals = cumsum([0,heights.*dt]);
F = spline(t, [0, Fvals, 0]);
DF = fnder(F);  % computes its first derivative
% h.String = 'h(i)';
% tL.String = 't(i)';
% tR.String = 't(i+1)';
hold on
fnplt(DF, 'r', 2)
hold off
ylims = ylim; 
ylim([0,ylims(2)]);
xlim([xmin xmax])
title('Tortelier 1952')
xticklabels('auto')
xticks(0:25:400)

%Piatigorsky
nexttile
y = Piatigorgskyrec195457;
y = add_noise(y);
hist(y, bins)
[heights,centers] = hist(y, bins);
hold on
ax = gca;
ax.XTickLabel = [];
n = length(centers);
w = centers(2)-centers(1);
t = linspace(centers(1)-w/2,centers(end)+w/2,n+1);
p = fix(n/2);
% fill(t([p p p+1 p+1]),[0 heights([p p]),0],'w')
% plot(centers([p p]),[0 heights(p)],'r:')
% h = text(centers(p)-.2,heights(p)/2,'   h');
% dep = -70;
% tL = text(t(p),dep,'L');
% tR = text(t(p+1),dep,'R');
hold off
dt = diff(t);
Fvals = cumsum([0,heights.*dt]);
F = spline(t, [0, Fvals, 0]);
DF = fnder(F);  % computes its first derivative
% h.String = 'h(i)';
% tL.String = 't(i)';
% tR.String = 't(i+1)';
hold on
fnplt(DF, 'r', 2)
hold off
ylims = ylim; 
ylim([0,ylims(2)]);
xlim([xmin xmax])
title('Piatigorsky 1954')
xticklabels('auto')
xticks(0:25:400)


%Casals 2
nexttile
y = Casalsrec1954;
y = add_noise(y);
hist(y, bins)
[heights,centers] = hist(y, bins);
hold on
ax = gca;
ax.XTickLabel = [];
n = length(centers);
w = centers(2)-centers(1);
t = linspace(centers(1)-w/2,centers(end)+w/2,n+1);
p = fix(n/2);
% fill(t([p p p+1 p+1]),[0 heights([p p]),0],'w')
% plot(centers([p p]),[0 heights(p)],'r:')
% h = text(centers(p)-.2,heights(p)/2,'   h');
% dep = -70;
% tL = text(t(p),dep,'L');
% tR = text(t(p+1),dep,'R');
hold off
dt = diff(t);
Fvals = cumsum([0,heights.*dt]);
F = spline(t, [0, Fvals, 0]);
DF = fnder(F);  % computes its first derivative
% h.String = 'h(i)';
% tL.String = 't(i)';
% tR.String = 't(i+1)';
hold on
fnplt(DF, 'r', 2)
hold off
ylims = ylim; 
ylim([0,ylims(2)]);
xlim([xmin xmax])
title('Casals 1954')
xticklabels('auto')
xticks(0:25:400)


%Nelsova
nexttile
y = Nelsovarec195556;
y = add_noise(y);
hist(y, bins)
[heights,centers] = hist(y, bins);
hold on
ax = gca;
ax.XTickLabel = [];
n = length(centers);
w = centers(2)-centers(1);
t = linspace(centers(1)-w/2,centers(end)+w/2,n+1);
p = fix(n/2);
% fill(t([p p p+1 p+1]),[0 heights([p p]),0],'w')
% plot(centers([p p]),[0 heights(p)],'r:')
% h = text(centers(p)-.2,heights(p)/2,'   h');
% dep = -70;
% tL = text(t(p),dep,'L');
% tR = text(t(p+1),dep,'R');
hold off
dt = diff(t);
Fvals = cumsum([0,heights.*dt]);
F = spline(t, [0, Fvals, 0]);
DF = fnder(F);  % computes its first derivative
% h.String = 'h(i)';
% tL.String = 't(i)';
% tR.String = 't(i+1)';
hold on
fnplt(DF, 'r', 2)
hold off
ylims = ylim; 
ylim([0,ylims(2)]);
xlim([xmin xmax])
title('Nelsova 1955')
xticklabels('auto')
xticks(0:25:400)


%Starker
nexttile
y = Starkerrec1959;
y = add_noise(y);
hist(y, bins)
[heights,centers] = hist(y, bins);
hold on
ax = gca;
ax.XTickLabel = [];
n = length(centers);
w = centers(2)-centers(1);
t = linspace(centers(1)-w/2,centers(end)+w/2,n+1);
p = fix(n/2);
% fill(t([p p p+1 p+1]),[0 heights([p p]),0],'w')
% plot(centers([p p]),[0 heights(p)],'r:')
% h = text(centers(p)-.2,heights(p)/2,'   h');
% dep = -70;
% tL = text(t(p),dep,'L');
% tR = text(t(p+1),dep,'R');
hold off
dt = diff(t);
Fvals = cumsum([0,heights.*dt]);
F = spline(t, [0, Fvals, 0]);
DF = fnder(F);  % computes its first derivative
% h.String = 'h(i)';
% tL.String = 't(i)';
% tR.String = 't(i+1)';
hold on
fnplt(DF, 'r', 2)
hold off
ylims = ylim; 
ylim([0,ylims(2)]);
xlim([xmin xmax])
title('Starker 1959')
xticklabels('auto')
xticks(0:25:400)

%Fournier 2
nexttile
y = PFournierrec1959;
y = add_noise(y);
hist(y, bins)
[heights,centers] = hist(y, bins);
hold on
ax = gca;
ax.XTickLabel = [];
n = length(centers);
w = centers(2)-centers(1);
t = linspace(centers(1)-w/2,centers(end)+w/2,n+1);
p = fix(n/2);
% fill(t([p p p+1 p+1]),[0 heights([p p]),0],'w')
% plot(centers([p p]),[0 heights(p)],'r:')
% h = text(centers(p)-.2,heights(p)/2,'   h');
% dep = -70;
% tL = text(t(p),dep,'L');
% tR = text(t(p+1),dep,'R');
hold off
dt = diff(t);
Fvals = cumsum([0,heights.*dt]);
F = spline(t, [0, Fvals, 0]);
DF = fnder(F);  % computes its first derivative
% h.String = 'h(i)';
% tL.String = 't(i)';
% tR.String = 't(i+1)';
hold on
fnplt(DF, 'r', 2)
hold off
ylims = ylim; 
ylim([0,ylims(2)]);
xlim([xmin xmax])
title('Fournier 1959')
xticklabels('auto')
xticks(0:25:400)


%Rostropovich
nexttile
y = Rostropovichrec1964;
y = add_noise(y);
hist(y, bins)
[heights,centers] = hist(y, bins);
hold on
ax = gca;
ax.XTickLabel = [];
n = length(centers);
w = centers(2)-centers(1);
t = linspace(centers(1)-w/2,centers(end)+w/2,n+1);
p = fix(n/2);
% fill(t([p p p+1 p+1]),[0 heights([p p]),0],'w')
% plot(centers([p p]),[0 heights(p)],'r:')
% h = text(centers(p)-.2,heights(p)/2,'   h');
% dep = -70;
% tL = text(t(p),dep,'L');
% tR = text(t(p+1),dep,'R');
hold off
dt = diff(t);
Fvals = cumsum([0,heights.*dt]);
F = spline(t, [0, Fvals, 0]);
DF = fnder(F);  % computes its first derivative
% h.String = 'h(i)';
% tL.String = 't(i)';
% tR.String = 't(i+1)';
hold on
fnplt(DF, 'r', 2)
hold off
ylims = ylim; 
ylim([0,ylims(2)]);
xlim([xmin xmax])
title('Rostropovich 1964')
xticklabels('auto')
xticks(0:25:400)


%Fournier 3
nexttile
y = Fournierrec1965;
y = add_noise(y);
hist(y, bins)
[heights,centers] = hist(y, bins);
hold on
ax = gca;
ax.XTickLabel = [];
n = length(centers);
w = centers(2)-centers(1);
t = linspace(centers(1)-w/2,centers(end)+w/2,n+1);
p = fix(n/2);
% fill(t([p p p+1 p+1]),[0 heights([p p]),0],'w')
% plot(centers([p p]),[0 heights(p)],'r:')
% h = text(centers(p)-.2,heights(p)/2,'   h');
% dep = -70;
% tL = text(t(p),dep,'L');
% tR = text(t(p+1),dep,'R');
hold off
dt = diff(t);
Fvals = cumsum([0,heights.*dt]);
F = spline(t, [0, Fvals, 0]);
DF = fnder(F);  % computes its first derivative
% h.String = 'h(i)';
% tL.String = 't(i)';
% tR.String = 't(i+1)';
hold on
fnplt(DF, 'r', 2)
hold off
ylims = ylim; 
ylim([0,ylims(2)]);
xlim([xmin xmax])
title('Fournier 1965')
xticklabels('auto')
xticks(0:25:400)


%Du Pre
nexttile
y = DuPreliveRec1970;
y = add_noise(y);
hist(y, bins)
[heights,centers] = hist(y, bins);
hold on
ax = gca;
ax.XTickLabel = [];
n = length(centers);
w = centers(2)-centers(1);
t = linspace(centers(1)-w/2,centers(end)+w/2,n+1);
p = fix(n/2);
% fill(t([p p p+1 p+1]),[0 heights([p p]),0],'w')
% plot(centers([p p]),[0 heights(p)],'r:')
% h = text(centers(p)-.2,heights(p)/2,'   h');
% dep = -70;
% tL = text(t(p),dep,'L');
% tR = text(t(p+1),dep,'R');
hold off
dt = diff(t);
Fvals = cumsum([0,heights.*dt]);
F = spline(t, [0, Fvals, 0]);
DF = fnder(F);  % computes its first derivative
% h.String = 'h(i)';
% tL.String = 't(i)';
% tR.String = 't(i+1)';
hold on
fnplt(DF, 'r', 2)
hold off
ylims = ylim; 
ylim([0,ylims(2)]);
xlim([xmin xmax])
title('Du Pre 1970')
xticklabels('auto')
xticks(0:25:400)


%Shafran
nexttile
y = Shafranrec1973;
y = add_noise(y);
hist(y, bins)
[heights,centers] = hist(y, bins);
hold on
ax = gca;
ax.XTickLabel = [];
n = length(centers);
w = centers(2)-centers(1);
t = linspace(centers(1)-w/2,centers(end)+w/2,n+1);
p = fix(n/2);
% fill(t([p p p+1 p+1]),[0 heights([p p]),0],'w')
% plot(centers([p p]),[0 heights(p)],'r:')
% h = text(centers(p)-.2,heights(p)/2,'   h');
% dep = -70;
% tL = text(t(p),dep,'L');
% tR = text(t(p+1),dep,'R');
hold off
dt = diff(t);
Fvals = cumsum([0,heights.*dt]);
F = spline(t, [0, Fvals, 0]);
DF = fnder(F);  % computes its first derivative
% h.String = 'h(i)';
% tL.String = 't(i)';
% tR.String = 't(i+1)';
hold on
fnplt(DF, 'r', 2)
hold off
ylims = ylim; 
ylim([0,ylims(2)]);
xlim([xmin xmax])
title('Shafran 1973')
xticklabels('auto')
xticks(0:25:400)


%Yo Yo Ma
nexttile
y = YoYoMa1985LiveRec;
y = add_noise(y);
hist(y, bins)
[heights,centers] = hist(y, bins);
hold on
ax = gca;
ax.XTickLabel = [];
n = length(centers);
w = centers(2)-centers(1);
t = linspace(centers(1)-w/2,centers(end)+w/2,n+1);
p = fix(n/2);
% fill(t([p p p+1 p+1]),[0 heights([p p]),0],'w')
% plot(centers([p p]),[0 heights(p)],'r:')
% h = text(centers(p)-.2,heights(p)/2,'   h');
% dep = -70;
% tL = text(t(p),dep,'L');
% tR = text(t(p+1),dep,'R');
hold off
dt = diff(t);
Fvals = cumsum([0,heights.*dt]);
F = spline(t, [0, Fvals, 0]);
DF = fnder(F);  % computes its first derivative
% h.String = 'h(i)';
% tL.String = 't(i)';
% tR.String = 't(i+1)';
hold on
fnplt(DF, 'r', 2)
hold off
ylims = ylim; 
ylim([0,ylims(2)]);
xlim([xmin xmax])
title('Yo Yo Ma')
xticklabels('auto')
xticks(0:25:400)


%Wispelwey
nexttile
y = Wispelweyrec1991;
y = add_noise(y);
hist(y, bins)
[heights,centers] = hist(y, bins);
hold on
ax = gca;
ax.XTickLabel = [];
n = length(centers);
w = centers(2)-centers(1);
t = linspace(centers(1)-w/2,centers(end)+w/2,n+1);
p = fix(n/2);
% fill(t([p p p+1 p+1]),[0 heights([p p]),0],'w')
% plot(centers([p p]),[0 heights(p)],'r:')
% h = text(centers(p)-.2,heights(p)/2,'   h');
% dep = -70;
% tL = text(t(p),dep,'L');
% tR = text(t(p+1),dep,'R');
hold off
dt = diff(t);
Fvals = cumsum([0,heights.*dt]);
F = spline(t, [0, Fvals, 0]);
DF = fnder(F);  % computes its first derivative
% h.String = 'h(i)';
% tL.String = 't(i)';
% tR.String = 't(i+1)';
hold on
fnplt(DF, 'r', 2)
hold off
ylims = ylim; 
ylim([0,ylims(2)]);
xlim([xmin xmax])
title('Wispelwey 1991')
xticklabels('auto')
xticks(0:25:400)


%Maisky
nexttile
y = Maiskyrec1992;
y = add_noise(y);
hist(y, bins)
[heights,centers] = hist(y, bins);
hold on
ax = gca;
ax.XTickLabel = [];
n = length(centers);
w = centers(2)-centers(1);
t = linspace(centers(1)-w/2,centers(end)+w/2,n+1);
p = fix(n/2);
% fill(t([p p p+1 p+1]),[0 heights([p p]),0],'w')
% plot(centers([p p]),[0 heights(p)],'r:')
% h = text(centers(p)-.2,heights(p)/2,'   h');
% dep = -70;
% tL = text(t(p),dep,'L');
% tR = text(t(p+1),dep,'R');
hold off
dt = diff(t);
Fvals = cumsum([0,heights.*dt]);
F = spline(t, [0, Fvals, 0]);
DF = fnder(F);  % computes its first derivative
% h.String = 'h(i)';
% tL.String = 't(i)';
% tR.String = 't(i+1)';
hold on
fnplt(DF, 'r', 2)
hold off
ylims = ylim; 
ylim([0,ylims(2)]);
xlim([xmin xmax])
title('Maisky 1992')
xticklabels('auto')
xticks(0:25:400)


%Bylsma
nexttile
y = BylsmaRec1998;
y = add_noise(y);
hist(y, bins)
[heights,centers] = hist(y, bins);
hold on
ax = gca;
ax.XTickLabel = [];
n = length(centers);
w = centers(2)-centers(1);
t = linspace(centers(1)-w/2,centers(end)+w/2,n+1);
p = fix(n/2);
% fill(t([p p p+1 p+1]),[0 heights([p p]),0],'w')
% plot(centers([p p]),[0 heights(p)],'r:')
% h = text(centers(p)-.2,heights(p)/2,'   h');
% dep = -70;
% tL = text(t(p),dep,'L');
% tR = text(t(p+1),dep,'R');
hold off
dt = diff(t);
Fvals = cumsum([0,heights.*dt]);
F = spline(t, [0, Fvals, 0]);
DF = fnder(F);  % computes its first derivative
% h.String = 'h(i)';
% tL.String = 't(i)';
% tR.String = 't(i+1)';
hold on
fnplt(DF, 'r', 2)
hold off
ylims = ylim; 
ylim([0,ylims(2)]);
xlim([xmin xmax])
title('Bylsma 1998')
xticklabels('auto')
xticks(0:25:400)


%Perenyi 
nexttile
y = Perenyirec2001;
y = add_noise(y);
hist(y, bins)
[heights,centers] = hist(y, bins);
hold on
ax = gca;
ax.XTickLabel = [];
n = length(centers);
w = centers(2)-centers(1);
t = linspace(centers(1)-w/2,centers(end)+w/2,n+1);
p = fix(n/2);
% fill(t([p p p+1 p+1]),[0 heights([p p]),0],'w')
% plot(centers([p p]),[0 heights(p)],'r:')
% h = text(centers(p)-.2,heights(p)/2,'   h');
% dep = -70;
% tL = text(t(p),dep,'L');
% tR = text(t(p+1),dep,'R');
hold off
dt = diff(t);
Fvals = cumsum([0,heights.*dt]);
F = spline(t, [0, Fvals, 0]);
DF = fnder(F);  % computes its first derivative
% h.String = 'h(i)';
% tL.String = 't(i)';
% tR.String = 't(i+1)';
hold on
fnplt(DF, 'r', 2)
hold off
ylims = ylim; 
ylim([0,ylims(2)]);
xlim([xmin xmax])
title('Perenyi 2001')
xticklabels('auto')
xticks(0:25:400)


%Kliegel
nexttile
y = Kilegelrec2002;
y = add_noise(y);
hist(y, bins)
[heights,centers] = hist(y, bins);
hold on
ax = gca;
ax.XTickLabel = [];
n = length(centers);
w = centers(2)-centers(1);
t = linspace(centers(1)-w/2,centers(end)+w/2,n+1);
p = fix(n/2);
% fill(t([p p p+1 p+1]),[0 heights([p p]),0],'w')
% plot(centers([p p]),[0 heights(p)],'r:')
% h = text(centers(p)-.2,heights(p)/2,'   h');
% dep = -70;
% tL = text(t(p),dep,'L');
% tR = text(t(p+1),dep,'R');
hold off
dt = diff(t);
Fvals = cumsum([0,heights.*dt]);
F = spline(t, [0, Fvals, 0]);
DF = fnder(F);  % computes its first derivative
% h.String = 'h(i)';
% tL.String = 't(i)';
% tR.String = 't(i+1)';
hold on
fnplt(DF, 'r', 2)
hold off
ylims = ylim; 
ylim([0,ylims(2)]);
xlim([xmin xmax])
title('Kliegel 2002')
xticklabels('auto')
xticks(0:25:400)


%Wispelwey 2
nexttile
y = Wispelweyrec2004;
y = add_noise(y);
hist(y, bins)
[heights,centers] = hist(y, bins);
hold on
ax = gca;
ax.XTickLabel = [];
n = length(centers);
w = centers(2)-centers(1);
t = linspace(centers(1)-w/2,centers(end)+w/2,n+1);
p = fix(n/2);
% fill(t([p p p+1 p+1]),[0 heights([p p]),0],'w')
% plot(centers([p p]),[0 heights(p)],'r:')
% h = text(centers(p)-.2,heights(p)/2,'   h');
% dep = -70;
% tL = text(t(p),dep,'L');
% tR = text(t(p+1),dep,'R');
hold off
dt = diff(t);
Fvals = cumsum([0,heights.*dt]);
F = spline(t, [0, Fvals, 0]);
DF = fnder(F);  % computes its first derivative
% h.String = 'h(i)';
% tL.String = 't(i)';
% tR.String = 't(i+1)';
hold on
fnplt(DF, 'r', 2)
hold off
ylims = ylim; 
ylim([0,ylims(2)]);
xlim([xmin xmax])
title('Wispelwey 2004')
xticklabels('auto')
xticks(0:25:400)


%Schott
nexttile
y = Schottrec20082009;
y = add_noise(y);
hist(y, bins)
[heights,centers] = hist(y, bins);
hold on
ax = gca;
ax.XTickLabel = [];
n = length(centers);
w = centers(2)-centers(1);
t = linspace(centers(1)-w/2,centers(end)+w/2,n+1);
p = fix(n/2);
% fill(t([p p p+1 p+1]),[0 heights([p p]),0],'w')
% plot(centers([p p]),[0 heights(p)],'r:')
% h = text(centers(p)-.2,heights(p)/2,'   h');
% dep = -70;
% tL = text(t(p),dep,'L');
% tR = text(t(p+1),dep,'R');
hold off
dt = diff(t);
Fvals = cumsum([0,heights.*dt]);
F = spline(t, [0, Fvals, 0]);
DF = fnder(F);  % computes its first derivative
% h.String = 'h(i)';
% tL.String = 't(i)';
% tR.String = 't(i+1)';
hold on
fnplt(DF, 'r', 2)
hold off
ylims = ylim; 
ylim([0,ylims(2)]);
xlim([xmin xmax])
title('Schott 2008')
xticklabels('auto')
xticks(0:25:400)


%Isserlis
nexttile
y = Isserlisrec2012;
y = add_noise(y);
hist(y, bins)
[heights,centers] = hist(y, bins);
hold on
ax = gca;
ax.XTickLabel = [];
n = length(centers);
w = centers(2)-centers(1);
t = linspace(centers(1)-w/2,centers(end)+w/2,n+1);
p = fix(n/2);
% fill(t([p p p+1 p+1]),[0 heights([p p]),0],'w')
% plot(centers([p p]),[0 heights(p)],'r:')
% h = text(centers(p)-.2,heights(p)/2,'   h');
% dep = -70;
% tL = text(t(p),dep,'L');
% tR = text(t(p+1),dep,'R');
hold off
dt = diff(t);
Fvals = cumsum([0,heights.*dt]);
F = spline(t, [0, Fvals, 0]);
DF = fnder(F);  % computes its first derivative
% h.String = 'h(i)';
% tL.String = 't(i)';
% tR.String = 't(i+1)';
hold on
fnplt(DF, 'r', 2)
hold off
ylims = ylim; 
ylim([0,ylims(2)]);
xlim([xmin xmax])
title('Isserlis 2012')
xticklabels('auto')
xticks(0:25:400)




