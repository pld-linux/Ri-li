Summary:	Ri-li arcade game
Summary(de):	Ri-li Arkade Spiel
Summary(pl):	Ri-li - gra zr�czno�ciowa
Name:		Ri-li
Version:	1.0.2
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/ri-li/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
# Source0-md5:	1be3222143eda9dc1569d7e04fbda159
URL:		http://www.ri-li.org
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Full-featured, 8 languages: Arabic, Chinese, English, French, German,
Japanese, Russian, Spanish. Colorful animated wood engine, 40 levels
in this first version and 3 beautiful musics and many sound effects.

%description -l de
Vollunterst�tzt, 8 Sprachen: Arabisch, Chinesisch, Englisch,
Franz�sisch, Deutsch, Japanisch, Russisch, Spanisch. Buntes lebendiges
Holz-Engine, 40 Levels in dieser ersten Version und 3 sch�ne
Begleitmusiken und viele tolle T�ne.

%description -l pl
Dopracowana, posiadaj�ca 8 wersji j�zykowych (arabsk�, chi�sk�,
angielsk�, francusk�, niemieck�, japo�sk�, rosyjsk� i hiszpa�sk�) gra
zr�czno�ciowa. Wyr�nia si� kolorow�-drewnopodobn� animowan� grafik�,
posiada 40 poziom�w, 3 �adne �cie�ki d�wi�kowe do wyboru oraz wiele
efekt�w d�wi�kowych.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}
install data/Ri-li-icon-16x16.png $RPM_BUILD_ROOT%{_pixmapsdir}
install data/Ri-li-icon-32x32.png $RPM_BUILD_ROOT%{_pixmapsdir}
install data/Ri-li-icon-48x48.png $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS NEWS
%attr(755,root,root) %{_bindir}/Ri_li
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/levels.dat
%{_datadir}/%{name}/sprites.dat
%{_datadir}/%{name}/Ri-li-icon-*.png
%{_datadir}/%{name}/*.ico
%{_datadir}/%{name}/Sounds
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}*.png
