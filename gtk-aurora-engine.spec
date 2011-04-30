%define libname %mklibname %{name}

Summary:	Aurora engine for Gtk 2.x
Name:		gtk-aurora-engine
Version:	1.5.1
Release:	%mkrel 1
Source0:	http://gnome-look.org/CONTENT/content-files/56438-aurora-%{version}.tar.bz2
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		http://gnome-look.org/content/show.php/Aurora+Gtk+Engine?content=56438
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	%{libname} = %{version}
BuildRequires:	gtk2-devel >= 2.12

%description
The goal of this theme is to provide a complete and consistent look
for Gtk. The theme aims to be very flexible in color choice, but
provide few other options otherwise. The theme includes some features
that do not seem to be available in other Gtk engines; it also allows
the theming of Gnome panel widgets.

%package -n %{libname}
Summary:    Library files for %{name}
Group:	    System/Libraries

%description -n %{libname}
Library files for %{name}.

%prep
%setup -qc %{name}-%{version}
tar xf *.tar.bz2
tar xf *.tar.gz

%build
pushd aurora-1.5
%configure2_5x --enable-animation
%make
popd

%install
%__rm -rf %{buildroot}
%makeinstall_std -C aurora-1.5
%__mkdir -p %{buildroot}%{_datadir}/themes
cp -fr Aurora %{buildroot}%{_datadir}/themes/

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc aurora-1.5/README aurora-1.5/ChangeLog
%{_datadir}/themes/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/gtk-2.0/*/engines/*.*
