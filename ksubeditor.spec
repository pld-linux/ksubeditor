Summary:	Ksubeditor is a DivX subtitle editor for KDE 3.x
Summary(pl):	Ksubeditor jest edytorem napisów dla KDE 3.x
Name:		ksubeditor
Version:	0.13
Epoch:		1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-c++.patch
Patch1:		%{name}-doc.patch	
# Source0-md5:	0849556d80e19ad3ce72909333aa584a
URL:		http://www.sourceforge.net/projects/ksubeditor/
BuildRequires:	fam-devel
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ksubeditor is a DivX subtitle editor for KDE 3.x. It is able to edit
and convert subtitles between different subtitle formats. It is able
to easily change the time of the subtitle and fit it to the movie.

%description -l pl
Ksubeditor jest edytorem napisów dla KDE 3.x. Jest w stanie
modyfikowaæ oraz konwertowaæ napisy pomiêdzy ró¿nymi formatami. Mo¿e w
prosty sposób zmieniaæ czas napisów oraz dopasowaæ je do filmu.

%prep
%setup -q -n %{name}-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install
install -d $RPM_BUILD_ROOT%{_desktopdir} 
# ,%{_pixmapsdir}/locolor/{16x16,32x32},%{_bindir}}
#install ksubeditor/lo16-app-ksubeditor.png $RPM_BUILD_ROOT%{_pixmapsdir}/locolor/16x16
#install ksubeditor/lo32-app-ksubeditor.png $RPM_BUILD_ROOT%{_pixmapsdir}/locolor/32x32
#install ksubeditor/ksubeditor $RPM_BUILD_ROOT%{_bindir}
mv -f $RPM_BUILD_ROOT%{_iconsdir}/{lo,hi}color
mv -f $RPM_BUILD_ROOT%{_datadir}/applnk/Applications/ksubeditor.desktop $RPM_BUILD_ROOT%{_desktopdir}/
echo "Categories=Qt;KDE;Utility;X-KDE-More" >> $RPM_BUILD_ROOT%{_desktopdir}/ksubeditor.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_defaultdocdir}/HTML/en/ksubeditor/*
%{_iconsdir}/hicolor/*/*
%{_desktopdir}/ksubeditor.desktop
