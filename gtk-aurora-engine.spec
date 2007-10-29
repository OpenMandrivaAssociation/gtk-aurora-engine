%define tarname aurora
%define name gtk-aurora-engine
%define version 1.2
%define release %mkrel 1

%define gtkbinaryver %(if $([ -x %{_bindir}/pkg-config ] && pkg-config --exists gtk+-2.0); then pkg-config --variable=gtk_binary_version gtk+-2.0; else echo 0; fi)

Summary: Aurora engine for Gtk 2.x
Name:    %{name}
Version: %{version}
Release: %{release}
Source0: %{tarname}-%{version}.tar.bz2
Source1: Gtkrc_themes.tar.bz2
License: GPL
Group: 	 Graphical desktop/Other
Url: 	 http://www.gnome-look.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gtk2-devel >= 2.10

%description
The goal of this theme is to provide a complete and consistent look
for Gtk. The theme aims to be very flexible in color choice, but
provide few other options otherwise. The theme includes some features
that do not seem to be available in other Gtk engines; it also allows
the theming of Gnome panel widgets.

%prep
%setup -q -n %{tarname}-%{version}

%build
%configure2_5x --enable-animation
%make

%install
%__rm -rf %{buildroot}
%makeinstall
%__mkdir -p %{buildroot}%{_datadir}/themes
%__tar jfx %SOURCE1 -C %{buildroot}%{_datadir}/themes

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README COPYING NEWS ChangeLog AUTHORS
%{_datadir}/themes/*
%{_libdir}/gtk-2.0/%{gtkbinaryver}/engines/*.*

